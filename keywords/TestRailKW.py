__author__ = 'nurgaliev'
import testrail as testrail
import time, sys, xlwt, os, re
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from xml.dom import minidom
from datetime import datetime

case_types = {1:'Automated', 2: 'Functionality', 6: 'Other'}

def add_project( name):
    data = {'name': name}
    return testrail.testrail_api('add_project', **data)


def add_run(project_name):
    project_id = get_project_id_by_name(project_name)
    case_ids = get_case_ids_by_types_for_project(project_id, [1,2])
    data = {'name':'tests_run_%s' % time.strftime('%Y%m%d_%X'), 'include_all':False, 'case_ids':case_ids}
    try:
        result = testrail.testrail_api('add_run', project_id, **data)
    except Exception,e:
        print 'ERORR in add_run: %s' % e
        return 0
    return result['id']


def get_case_ids_by_types_for_project(project_id,list_types):
    case_infos = get_tests_for_project_by_type(project_id, list_types)
    case_ids = [item['id'] for item in case_infos]
    return case_ids

def get_tests_for_project_by_type(project_id, list_case_type):
    data = {'type_id':','.join(str(e) for e in list_case_type)}
    try:
        result = testrail.testrail_api('get_cases', project_id, **data)
    except Exception,e:
        print 'ERORR in get_tests_for_project_by_type: %s' % e
        return 0
    return result


def get_project_id_by_name(project_name):
    "Get the project ID using project name"
    projects = testrail.testrail_api('get_projects')
    for project in projects:
        if project['name'] == project_name:
            project_id = project['id']
            break
    return project_id


def get_case_id_by_name(project_name, case_name):
    proj_id = get_project_id_by_name(project_name)
    cases = testrail.testrail_api('get_cases', proj_id)
    for case in cases:
        if case['title'] == case_name:
            return case['id']


def get_run_id(test_run_name,project_name):
    "Get the run ID using test name and project name"
    run_id=None
    project_id = get_project_id_by_name( project_name)
    args = [project_id]
    try:
        test_runs = testrail.testrail_api('get_runs', project_id)  #*args
    except Exception,e:
        print 'Exception in get_run_id() updating TestRail.'
        print 'PYTHON SAYS: '
        print e
        return None
    else:
        for test_run in test_runs:
             if test_run['name'] == test_run_name:
                 run_id = test_run['id']
                 break
        return run_id

def get_run_name(run_id):
    try:
        result = testrail.testrail_api('get_run', run_id)
    except Exception,e:
        print 'ERORR in get_run: %s' % e
        return 0
    return result['name']


def get_tests_by_run(run_id):
    try:
        result = testrail.testrail_api('get_tests', run_id)
    except Exception,e:
        print 'ERORR in get_tests_by_run: %s' % e
        return 0
    return result

def update_test_case(test_id, *args):
    assert(len(args)%2 == 0), 'WRONG number parameters in *args'
    data_dict = {args[i]:args[i+1] for i in range(0, len(args), 2)}
    try:
        result = testrail.testrail_api('update_case', test_id, **data_dict)
    except Exception,e:
        print 'ERORR in update_test_case: %s' % e
        return 0
    return result


def create_report(run_id, release_name, total_time=0):
    header_border = xlwt.Borders()
    header_border.bottom = xlwt.Borders.DOUBLE
    header_border.top = xlwt.Borders.DOUBLE
    header_border.right = xlwt.Borders.DOUBLE
    header_border.left = xlwt.Borders.DOUBLE

    header_font = xlwt.Font()
    header_font.bold = True

    aligment_center = xlwt.Alignment()
    aligment_center.horz = xlwt.Alignment.HORZ_CENTER

    table_header = xlwt.XFStyle()
    table_header.font = header_font
    table_header.borders = header_border
    table_header.alignment = aligment_center

    RED = 0x0A
    red_font = xlwt.Font()
    red_style = xlwt.XFStyle()
    red_style.font = red_font
    shaded_fill = xlwt.Pattern()
    shaded_fill.pattern = xlwt.Pattern.SOLID_PATTERN
    shaded_fill.pattern_fore_colour = RED
    red_style.pattern = shaded_fill

    footer_font = xlwt.Font()
    footer_font.bold = True
    table_footer = xlwt.XFStyle()
    table_footer.font = footer_font

    fields = ['number', 'case_id', 'title', 'status_id']
    statuses = {1: 'passed', 5: 'failed', 3: 'Untested'}
    wb = xlwt.Workbook()
    auto_sheet = wb.add_sheet('Auto_tests')
    man_sheet = wb.add_sheet('Manual_tests')
    for i, field_name in enumerate(fields):
        auto_sheet.write(0, i, field_name, table_header)
        man_sheet.write(0, i, field_name, table_header)
    auto_sheet.col(2).width = 12000
    man_sheet.col(2).width = 12000

    test_results = get_tests_by_run(run_id)
    count_failed_tests = 0
    list_failed_tests = []
    auto_row = 0
    man_row = 0
    for result in test_results:
        if result['type_id'] == 1:
            auto_row += 1
            for cell, field in enumerate(fields):
                if cell == 0:
                    auto_sheet.write(auto_row, cell, auto_row)
                elif cell == 3:
                    if result[field] in [3,5]:
                        list_failed_tests.append(result['title'])
                        count_failed_tests += 1
                        auto_sheet.write(auto_row, cell, statuses[result[field]], red_style)
                    else:
                        auto_sheet.write(auto_row, cell, statuses[result[field]])
                else:
                    auto_sheet.write(auto_row, cell, result[field])
        else:
            man_row += 1
            for cell, field in enumerate(fields):
                if cell == 0:
                    man_sheet.write(man_row, cell, man_row)
                elif cell == 3:
                    man_sheet.write(man_row, cell, statuses[1])
                else:
                    man_sheet.write(man_row, cell, result[field])
    man_total_string = 'Tests total/passed/failed: %d/%d/%d' % (man_row, man_row, 0)
    auto_total_string = 'Tests total/passed/failed: %d/%d/%d\n\n' % (auto_row, auto_row-count_failed_tests, count_failed_tests)
    man_sheet.write(man_row + 2, 2, man_total_string, table_header)
    auto_sheet.write(auto_row + 2, 2, auto_total_string, table_header)
    if len(list_failed_tests) != 0:
        auto_total_string+='    Failed tests:\n'
        for i,test in enumerate(list_failed_tests):
            auto_total_string += '%d.%s\n' % (i+1, test)
    if total_time:
        auto_total_string += '\n   Total elapsed time: %s' % total_time
    print auto_total_string
    output_file = '%s_tests_result_%s.xls' % (release_name, time.strftime('%Y%m%d_%H%M'))
    wb.save(output_file)
    return [output_file, auto_total_string]


def send_mail(send_from, send_to, subject, text, files=None,
              server="10.128.4.20"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def parse_xml_and_update_tests(xml_name, run_id):
    print os.path.abspath(__file__)
    path_to_xml = '%s/RobotTests/output/%s' % ('/'.join(os.path.abspath(__file__).split('/')[:-2]), xml_name)
    dom = minidom.parse(path_to_xml)
    dom.normalize()
    statuses = dom.getElementsByTagName('status')
    for status in statuses:
        if status.parentNode.localName == 'suite' and status.parentNode.getAttribute('id') == 's1':
            start_time = status.getAttribute('starttime')[:-4]
            end_time = status.getAttribute('endtime')[:-4]
            delta = datetime.strptime(end_time, '%Y%m%d %X') - datetime.strptime(start_time, '%Y%m%d %X')
            break
    nodes = dom.getElementsByTagName('test')
    case_ids_in_run = [item['case_id'] for item in get_tests_by_run(run_id)]
    test_list=[]
    for node in nodes:
        test_dict={}
        #test_dict['name'] = node.getAttribute('name')
        for child in node.childNodes:
            if child.nodeName == 'status':
                test_dict['status_id'] = 1 if child.getAttribute('status') == 'PASS' else 5
                child_start_time = child.getAttribute('starttime')[:-4]
                child_end_time = child.getAttribute('endtime')[:-4]
                delta_time = datetime.strptime(child_end_time, '%Y%m%d %X') - datetime.strptime(child_start_time,'%Y%m%d %X')
                total_seconds = int(delta_time.total_seconds())
                if total_seconds < 60:
                    time = "%ss" % total_seconds
                    if time == "0s":
                        time = "1s"
                else:
                    mins = total_seconds // 60
                    seks = total_seconds % 60
                    time = '%sm%ss' % (mins,seks)
                test_dict['elapsed'] = time
            elif child.nodeName == 'doc':
                if child.firstChild is None:
                    case_name = node.getAttribute('name')
                    print 'WARNING: test case %s has no ID' % case_name
                    case_id = get_case_id_by_name('SignServer', case_name)
                else:
                    case_id = int(child.firstChild.data[1:])
                if case_id in case_ids_in_run:
                    test_dict['case_id'] = case_id

            if len(test_dict) == 3:
                test_list.append(test_dict)
                break
    print test_list
    print len(test_list)
    data = {'results':test_list}
    testrail.testrail_api('add_results_for_cases', run_id, **data)
    return delta


def close_run_send_mail(run_id, proj_name, list_send_to):
    print 0
    total_time = parse_xml_and_update_tests('output.xml', run_id)
    print 1
    report_info = create_report(run_id, proj_name,  total_time)
    print 2
    report_name = report_info[0]
    print 3
    report_msg = report_info[1]
    print 4
    send_mail('jenkins@iksatprof.ru', list_send_to, '%s - autotests report' % proj_name, report_msg, [report_name])
    print 5
    return 1


if __name__=='__main__':
    command = sys.argv[1]
    if command == 'start_run':
        proj_name = re.sub('[\d\s\.]+', '', sys.argv[2]).strip()
        run_id = add_run(proj_name)
        print run_id
    elif command == 'close_run':
        print "=====Preparing report and sending email====="
        try:
            if len(sys.argv) > 3:
                run_id_input = int(sys.argv[2])
                release_name = sys.argv[3]
                proj_name = re.sub('[\d\s\.]+', '', release_name)
                list_send_to = sys.argv[4:]
                close_run_send_mail(run_id_input, proj_name, list_send_to)
        except Exception,e:
            print 'ERROR in close_run_send_mail:', e
            send_mail('jenkins@iksatprof.ru', list_send_to, '%s - autotests report' % proj_name, 'Unknown ERROR in send mail with test_report: %s' % e)
    else:
        print 'Wrong command name'


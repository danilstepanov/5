import time
from datetime import date
from requests import post
import requests
import shutil
from ssrv_orm import *
from sqlalchemy import asc, desc
import random
import KeyLadder as kl
import system_command
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from string import ascii_letters

any_string = lambda size: ''.join(choice(ascii_letters) for i in range(size))

def get_number_group(sqlalchemy_con):
    return sqlalchemy_con.session.query(Group).count()

def get_number_permission(sqlalchemy_con):
    return sqlalchemy_con.session.query(Permission).count()

def get_number_user(sqlalchemy_con):
    return sqlalchemy_con.session.query(User).count()

def get_number_user_groups(sqlalchemy_con):
    return sqlalchemy_con.session.query(Groups).count()

def get_number_user_user_permission(sqlalchemy_con):
    return sqlalchemy_con.session.query(UserUserPermissions).count()

def get_number_signserver_permission(sqlalchemy_con):
    return sqlalchemy_con.session.query(SignServerPermission).count()

def get_number_signserver_productgroup(sqlalchemy_con):
    return sqlalchemy_con.session.query(ProductGroup).count()

def get_number_signserver_signscript(sqlalchemy_con):
    return sqlalchemy_con.session.query(SignScript).count()

def get_number_signserver_sproduct(sqlalchemy_con):
    return sqlalchemy_con.session.query(Sproduct).count()

def get_number_signserver_sproduct_email(sqlalchemy_con):
    return sqlalchemy_con.session.query(SproductEmail).count()

def get_number_signserver_sign_file(sqlalchemy_con):
    return sqlalchemy_con.session.query(SignFile).count()

def get_number_fwkeys_firmware_keys(sqlalchemy_con):
    return sqlalchemy_con.session.query(FirmwarKeys).count()


def check_added_user(sqlalchemy_con, username):
    try:
        assert( username == sqlalchemy_con.session.query(User.username).filter(User.username == username).one()[0])
        return 1
    except Exception as e:
        return 0


def get_any_user(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(User.username).filter(User.username != None).all())[0]

def get_any_user_id_from_permission(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(SignServerPermission.user_id).all())[0]

def get_any_username_with_permission(sqlalchemy_con):
    user_id = get_any_user_id_from_permission(sqlalchemy_con)
    return sqlalchemy_con.session.query(User.username).filter(User.id == user_id).one()[0]

def get_any_superuser(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(User.username).filter(User.username != None, User.is_superuser == True).all())[0]

def get_username_without_permission(sqlalchemy_con):
    user_id = random.choice(sqlalchemy_con.session.query(User.id).filter(~User.id.in_(sqlalchemy_con.session.query(SignServerPermission.user_id).all())).all())[0]
    return sqlalchemy_con.session.query(User.username).filter(User.id == user_id).one()[0]

def get_any_sproduct(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(Sproduct.name).filter(Sproduct.name !=None).all())[0]

def get_any_productgroup(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(ProductGroup.name).filter(ProductGroup.name != None).all())[0]

def get_any_signscript(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(SignScript.name).filter(SignScript.name != None).all())[0]

def get_any_permission_id(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(SignServerPermission.id).filter(SignServerPermission.id != None).all())[0]

def get_project_last_signing(sqlalchemy_con):
    project_id = sqlalchemy_con.session.query(SignFile.product_id).filter(SignFile.id == max(sqlalchemy_con.session.query(SignFile.id).order_by(asc(SignFile.id)).all())[0]).one()[0]
    return sqlalchemy_con.session.query(Sproduct.name).filter(Sproduct.id == project_id).one()[0]


def get_sproduct_by_permission_id(sqlalchemy_con, permission_id):
    sproduct_id = sqlalchemy_con.session.query(SignServerPermission.product_id).filter(SignServerPermission.id == permission_id).one()[0]
    return sqlalchemy_con.session.query(Sproduct.name).filter(Sproduct.id == sproduct_id).one()[0]

def get_username_by_permission_id(sqlalchemy_con, permission_id):
    user_id = sqlalchemy_con.session.query(SignServerPermission.user_id).filter(SignServerPermission.id == permission_id).one()[0]
    return sqlalchemy_con.session.query(User.username).filter(User.id == user_id).one()[0]

def get_permission_status_by_permission_id(sqlalchemy_con, permission_id):
    return sqlalchemy_con.session.query(SignServerPermission.can_approve).filter(SignServerPermission.id == permission_id).one()[0]

def get_any_permission_id_without_sign_and_approve(sqlalchemy_con):
    return random.choice(sqlalchemy_con.session.query(SignServerPermission.id).filter(SignServerPermission.can_sign == False, SignServerPermission.can_approve == False).all())[0]

def check_db_userinfo(sqlalchemy_con, username, firstname, lastname, email):
    userinfo = sqlalchemy_con.session.query(User.username, User.first_name, User.last_name, User.email).filter(User.first_name == firstname, User.last_name == lastname, User.email == email).all()
    for i in userinfo:
        assert(username == i[0]), 'wrong username'
        assert(firstname == i[1]), 'wrong firstname'
        assert(lastname == i[2]), 'wrong lastname'
        assert(email == i[3]), 'wrong email'
    return 1

def check_db_script(sqlalchemy_con, signscript_name):
    signscript = sqlalchemy_con.session.query(SignScript.name).filter(SignScript.name == signscript_name).one()[0]
    assert(signscript == signscript_name), 'Wrong Signscript name in db'
    return 1

def check_db_productgroup(sqlalchemy_con, name):
    productgroup_id = sqlalchemy_con.session.query(ProductGroup.id).filter(ProductGroup.name == name).one()[0]
    assert(productgroup_id is not None)
    return 1


def check_db_sproduct(sqlalchemy_con, name, status):
    row = sqlalchemy_con.session.query(Sproduct.aprove_needed).filter(Sproduct.name == name).one()[0]
    assert(str(row) == str(status)), 'wrong status sproduct in db'
    return 1

def check_db_permission(sqlalchemy_con, username, sproduct, status):
    user_id = sqlalchemy_con.session.query(User.id).filter(User.username == username).one()[0]
    sproduct_id = sqlalchemy_con.session.query(Sproduct.id).filter(Sproduct.name == sproduct).one()[0]
    permission = sqlalchemy_con.session.query(SignServerPermission.can_approve).filter(SignServerPermission.user_id == user_id, SignServerPermission.product_id == sproduct_id).one()[0]
    assert(str(permission) == str(status)), 'Wrong status permission in DB'
    return 1

def check_filter_history(sqlalchemy_con, status, filter_from_web):
    if status == 'Failed':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).filter(SignFile.aprove == False, SignFile.refuse == False, SignFile.ready == False, SignFile.fail == True).order_by(desc(SignFile.id)).limit(400).all()
    elif status == 'Ready':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).filter(SignFile.refuse == False, SignFile.ready == True, SignFile.fail == False).order_by(desc(SignFile.id)).limit(400).all()
    elif status == 'Approved':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).filter(SignFile.aprove == True, SignFile.refuse == False, SignFile.ready == True, SignFile.fail == False).order_by(desc(SignFile.id)).limit(400).all()
    elif status == 'Refused':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).filter(SignFile.aprove == False, SignFile.refuse == True, SignFile.ready == True, SignFile.fail == False).order_by(desc(SignFile.id)).limit(400).all()
    elif status == 'Waiting':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).filter(SignFile.aprove == False, SignFile.refuse == False, SignFile.ready == False, SignFile.fail == False).order_by(desc(SignFile.id)).limit(400).all()
    elif status == 'Waiting approval':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).filter(SignFile.aprove == False, SignFile.refuse == False, SignFile.ready == True, SignFile.fail == False).order_by(desc(SignFile.id)).limit(400).all()
    elif status == 'All':
        db_fullfile_names = sqlalchemy_con.session.query(SignFile.blank_file).order_by(desc(SignFile.id)).limit(400).all()
    else:
        return 'Please, choose correct status'
    if len(filter_from_web) != len(db_fullfile_names):
        print "ERROR the lists are NOT equal!!!!! Len from web = %d, Len from db = %d" % (len(filter_from_web), len(db_fullfile_names))
        return 0
    db_file_names = [file[0].split('/')[-1] for file in db_fullfile_names]
    for web_file in filter_from_web:
        assert (web_file[0] in db_file_names), 'ERROR the list items are NOT equal!!!!!'
    return 1

def post_signing(sqlalchemy_con, sign_file, user, paswd, download, drm):
    id = random.choice(sqlalchemy_con.session.query(Sproduct.id).filter(Sproduct.id.in_(sqlalchemy_con.session.query(SproductEmail.sproduct_id).all()), Sproduct.name != 'fail', Sproduct.name != 'waiting', Sproduct.aprove_needed == False, Sproduct.is_drm == False).all())[0]
    #id_drm = random.choice(sqlalchemy_con.session.query(Sproduct.id).filter(Sproduct.id.in_(sqlalchemy_con.session.query(SproductEmail.sproduct_id).all()), Sproduct.name != 'fail', Sproduct.name != 'waiting', Sproduct.aprove_needed == False, Sproduct.is_drm == True).all())[0]
    project_name = sqlalchemy_con.session.query(Sproduct.name).filter(Sproduct.id == id).one()[0]
    # url = 'https://192.168.56.101/signserver/send_file'
    url = 'https://192.168.14.42/signserver/send_file'
    files = {'blank_file': open(sign_file)}
    if drm is True:
        data = {'product': '56', 'comment': 'THIS IS LOADED BY API DRM', 'version_field': '999', 'date_from': '2010-10-10', 'casstbids': '1', 'date_to':'2020-10-10'}
    else:
        data = {'product': id, 'comment': 'THIS IS LOADED BY API', 'version_field': '999'}
    r = post(url, files=files, data=data, auth=(user, paswd), cert=('/home/stp/test/username.usersurname.cifratech.com.crt', '/home/stp/test/username.usersurname.cifratech.com.key'), verify='/home/stp/test/cifraRootAndSignServer.crt',)
    time.sleep(6)
    if download is not None:
        aaa = r.text.split(',')[0]
        id_signfile = aaa.split(':')[1]
        download_url = get_url_for_download(user, paswd, id_signfile)
        if download_signfile_post(user, paswd, download_url) == 1:
            return 1
        else:
            return 0
    else:
        return project_name

def get_url_for_download(user, passwd, id_signfile):
    time.sleep(10)
    url = 'https://192.168.14.42:443/signserver/send_file'
    params = {'sign_file_id': id_signfile}
    response = requests.get(url=url, params=params, auth=(user, passwd), timeout=3, cert=('/home/stp/test/username.usersurname.cifratech.com.crt', '/home/stp/test/username.usersurname.cifratech.com.key'), verify='/home/stp/test/cifraRootAndSignServer.crt')
    return response.text.split('"')[-2]

def download_signfile_post(user, passwd, download_url):
    url_login = 'https://192.168.14.42/'
    client = requests.session()
    client.get(url_login, cert=('/home/stp/test/username.usersurname.cifratech.com.crt', '/home/stp/test/username.usersurname.cifratech.com.key'), verify='/home/stp/test/cifraRootAndSignServer.crt')
    login_data = {'username': user, 'password': passwd, 'csrfmiddlewaretoken': client.cookies['csrftoken']}
    login_request = client.post(url_login, auth=(user, passwd), data=login_data, headers={'Referer': url_login}, cert=('/home/stp/test/username.usersurname.cifratech.com.crt', '/home/stp/test/username.usersurname.cifratech.com.key'), verify='/home/stp/test/cifraRootAndSignServer.crt')
    if '<input class="input_box" id="id_password" name="password" type="password" /> ' not in login_request.content:
        if login_request.status_code == 200:
            print "User login success"
        else:
            print 'POST login: code {0}'.format(login_request.status_code)
    else:
        print "User login fails"
    url_file = '%s%s' % ('https://', download_url)
    sessionid = client.cookies['sessionid']
    r = client.get(url_file, cookies={'sessionid': sessionid}, stream=True)
    print 'GET file: result({0}) content-type({1})'.format(r.status_code, r.headers['content-type'])
    print "Downloading starts"
    local_filename = url_file.split('/')[-1]
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    return 1

def login_to_sign(driver):
    driver.get("https://192.168.14.42:443")
    driver.find_element_by_id("id_username").send_keys('stp')
    driver.find_element_by_id("id_password").send_keys('1')
    driver.find_element_by_class_name("main").click()
    return driver

def login_to_admin(driver):
    driver.get("https://192.168.14.42:443/admin")
    driver.find_element_by_id("id_username").send_keys('stp')
    driver.find_element_by_id("id_password").send_keys('1')
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    return driver

def check_sort_in_history(sqlalchemy_con,table_from_site, type_to_sort):
    count = 0
    if type_to_sort == 'Project':
        file_name = sqlalchemy_con.session.query(SignFile.blank_file, ProductGroup.name, SignFile.comment).order_by(asc(ProductGroup.name)).filter(Sproduct.id == SignFile.product_id).all()
        for item in table_from_site:
            assert(item[0] == str(file_name[count][0]).split('/')[-1]), 'Wrong file name in DB'
            #assert(item[2] == file_name[count][1]), 'Wrong project id in db'
            #assert(item[2] == file_name[count][2]), 'Wrong comment in db'
            count += 1
        return 1
    elif type_to_sort == 'Version':
        file_name = sqlalchemy_con.session.query(SignFile.version_field).order_by(asc(SignFile.version_field)).all()
        for item in table_from_site:
            assert (item[3] == file_name[count][0]), 'Wrong Version in db'
            count += 1
        return 1
    else:
        file_name = sqlalchemy_con.session.query(SignFile.blank_file, SignFile.comment, SignFile.product_id).order_by(asc(getattr(SignFile,type_to_sort))).all()
    for item in table_from_site:
        assert(item[0] == str(file_name[count][0]).split('/')[-1]), 'Wrong file name in DB'
        #print(item[1].split('/')[1])
        #assert(sqlalchemy_con.session.query(Sproduct.id).filter(Sproduct.name == item[1].split('/')[1]).one()[0] == file_name[count][2]), 'Wrong project id in db'
        assert(item[2] == file_name[count][1]), 'Wrong comment in db'
        count += 1
    return 1

def check_sort_in_approval(sqlalchemy_con, list_filter, type_to_sort):
    count = 0
    if type_to_sort == 'File name':
        file_name = sqlalchemy_con.session.query(SignFile.blank_file, SignFile.product_id).order_by(asc(SignFile.blank_file)).all()
    elif type_to_sort == 'Project':
        file_name = sqlalchemy_con.session.query(SignFile.blank_file, SignFile.product_id).order_by(asc(ProductGroup.name)).filter(Sproduct.id == SignFile.product_id).all()
    else:
        return 'Error sort choose correct "File name", "Project", "default"'
    print file_name
    for item in list_filter:
        assert(item[0] == str(file_name[count][0]).split('/')[-1]), 'Wrong file name in DB'
        assert(sqlalchemy_con.session.query(Sproduct.id).filter(Sproduct.name == item[2]).one()[0] == file_name[count][1]), 'Wrong project id in db'
        count += 1
    return 1

def change_comment(sqlalchemy_con, comment):
    t1 = datetime.now()
    while (datetime.now() - t1).seconds <= 15:
        time.sleep(0.3)
        try:
            buff = sqlalchemy_con.session.query(SignFile.id).filter(SignFile.comment == comment).one()[0]
            if buff is not None:
                return 1
        except:
            continue
    return 0


def prep_to_test_with_fw_keys():
    assert (system_command.docker_cp_to_ssrv_lib_hasp('kmi_file11.dat') == 1), "kmi_file11.dat was not copied"
    assert (system_command.docker_cp_to_ssrv_lib_hasp('kmi_file12.dat') == 1), "kmi_file12.dat was not copied"
    assert (system_command.docker_cp_to_ssrv_lib_hasp('bbmk.dat') == 1), "bbmk.dat was not copied"

def copy_fw_key_to_host():
    assert (system_command.docker_cp_from_ssrv_lib_hasp('/media/output.dat') == 1), "output.dat was not copied"
    path_to_file_on_host = '%s%s' %  (system_command.get_homedir_out(), '/output.dat')
    return path_to_file_on_host

def copy_fwrom_key_to_host():
    assert (system_command.docker_cp_from_ssrv_lib_hasp('/media/output.dat.kdf') == 1), "output.dat.kdf was not copied"
    path_to_file_on_host = '%s%s' %  (system_command.get_homedir_out(), '/output.dat.kdf')
    return path_to_file_on_host

def check_fw_key(sqlalchemy_con, key_id, rom):
    #path_to_file_on_host = copy_fw_key_to_host()
    path_to_file_on_host = '/home/stp/out/output.dat'
    buff = sqlalchemy_con.session.query(FirmwarKeys.key_value).filter(FirmwarKeys.fwky_id == key_id).one()[0]
    clean_fwkey = kl.KeyLadder().decrypt_buf_by_kmi_ladder(buff, key_id)
    ssrv_lib_key = open(path_to_file_on_host, 'rb').read()
    assert(clean_fwkey == ssrv_lib_key), 'Error, differents FW keys'
    if rom is not None:
        count = 0
        path_to_file_on_host_rom = copy_fwrom_key_to_host()
        rom_parametr = sqlalchemy_con.session.query(FirmwarKeys.rom_key_index, FirmwarKeys.rom_id).filter(FirmwarKeys.fwky_id == key_id).one()
        with open(path_to_file_on_host_rom, 'r') as f:
            for lines in f:
                assert (int(lines) == rom_parametr[count]), "ERROR in kdf file"
                count += 1
    return 1

def get_last_signfile_id(sqlalchemy_con):
    return max(sqlalchemy_con.session.query(SignFile.id).all())[0]

def check_script_ready(sqlalchemy_con, id):
    id = id + 1
    t1 = datetime.now()
    while (datetime.now() - t1).seconds <= 15:
        time.sleep(0.3)
        try:
            buff = sqlalchemy_con.session.query(SignFile.ready, SignFile.fail).filter(SignFile.id == id).all()[0]
            if buff == (True, False):
                return 1
        except:
            continue
    return 0


def check_script_refuse(sqlalchemy_con, id):
    id = id + 1
    t1 = datetime.now()
    while (datetime.now() - t1).seconds <= 15:
        time.sleep(0.3)
        try:
            buff = sqlalchemy_con.session.query(SignFile.aprove, SignFile.refuse, SignFile.ready, SignFile.fail).filter(SignFile.id == id).all()[0]
            if buff == (False, True, True, False):
                return 1
        except:
            continue
    return 0

def click_delete():
    driver = Chrome()
    login_to_sign(driver)
    driver.find_element_by_class_name("ico_menuApproval").click()
    driver.find_element_by_id("delete1").click()
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        print e
        return 0



def get_path(filename, files):
    for item in files:
        if filename in item[0]:
            return item[0]

def delete_sign_file(sqlalchemy_con, last_signed):
    driver = Chrome()
    login_to_sign(driver)
    driver.find_element_by_partial_link_text('Approval').click()
    select = Select(driver.find_element_by_name('sort_type_approval'))
    select.select_by_visible_text('Approved')
    table = driver.find_element_by_class_name("maintable")
    table_rows = table.find_elements_by_tag_name('tr')
    row_in_table = random.randint(1, (len(table_rows)-1))
    headers = table_rows[0]
    cells = headers.find_elements_by_tag_name('th')
    index_comment = 1
    for cell in cells:
        if cell.text == 'File':
            break
        index_comment +=1
    if last_signed is not None:
        file_name_on_site = table.find_element_by_xpath('.//tbody/tr[2]/td[2]')
    else:
        file_name_on_site = table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]' % (row_in_table + 1, index_comment))
    files = sqlalchemy_con.session.query(SignFile.blank_file).all()
    path = get_path(file_name_on_site.text, files)
    print 0
    copy_file = system_command.docker_cp_from_ssrv_web(path)
    print 1
    if copy_file == 1:
        button_del = "%s%s" % ('delete', row_in_table)
        driver.find_element_by_id(button_del).click()
        try:
            driver.switch_to_alert().accept()
        except Exception as e:
            print e
            return 0
    else:
        return 'signfile does not exist'
    driver.find_element_by_class_name('ico_baseExit').click()
    driver.close()
    try:
        system_command.docker_cp_from_ssrv_web(path)
        return 'File was not deleted from container ssrv_web'
    except:
        return 1

def wait_until_page_contain_error(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "errornote")))
        return 1
    except Exception as e:
        return 0

def add_no_active_user_trying_him_to_login():
    driver = Chrome()
    login_to_admin(driver)
    username = any_string(10)
    passwd = any_string(5)
    driver.find_element_by_class_name('addlink').click()
    driver.find_element_by_id('id_username').send_keys(username)
    driver.find_element_by_id('id_password1').send_keys(passwd)
    driver.find_element_by_id('id_password2').send_keys(passwd)
    driver.find_element_by_name('_continue').click()
    time.sleep(3)
    driver.find_element_by_id('id_is_active').click()
    driver.find_element_by_name('_save').click()
    driver.find_element_by_link_text('LOG OUT').click()
    driver.find_element_by_link_text('Log in again').click()
    driver.find_element_by_id('id_username').send_keys(username)
    driver.find_element_by_id('id_password').send_keys(passwd)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
    assert (wait_until_page_contain_error(driver) == 1), "no error message is displayed"
    driver.close()
    return 1

def check_imported_fwkeys_version_one(sqlalchemy_con, path_to_file, count, start_id):
    final_id = count + start_id
    keys_value = sqlalchemy_con.session.query(FirmwarKeys.key_value).order_by(asc(FirmwarKeys.fwky_id)).filter(FirmwarKeys.fwky_id >= start_id, FirmwarKeys.fwky_id < final_id).all()
    list_keys_db = []
    list_keys_file = []
    for item in keys_value:
        list_keys_db.append(str(item[0]).encode('hex'))
    with open(path_to_file, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            list_keys_file.append(line.split(';')[1][:-1])
    assert (list_keys_file == list_keys_db), ("ERROR, list keys not the same", list_keys_file, 'file<<<>>>db', list_keys_db)
    return 1

def check_imported_fwkeys_version_two(sqlalchemy_con, path_to_file, count, start_id):
    final_id = count + start_id
    keys_value = sqlalchemy_con.session.query(FirmwarKeys.key_value, FirmwarKeys.rom_key_index, FirmwarKeys.rom_id).order_by(asc(FirmwarKeys.fwky_id)).filter(FirmwarKeys.fwky_id >= start_id, FirmwarKeys.fwky_id < final_id).all()
    list_keys_db = []
    list_keys_file = []
    for item in keys_value:
        key_str = ('%s;%s;%s;' % (str(item[0]).encode('hex'), item[1], item[2]))
        list_keys_db.append(key_str.replace(';-1', ';'))
    with open(path_to_file, 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            line = line.split(';')[:-1]
            list_keys_file.append('%s;%s;%s;' % (line[1], line[2], line[3]))
    assert (list_keys_db == list_keys_file), 'ERROR, list keys not the same'
    return 1

def get_count_of_key_value(sqlalchemy_con):
    return len(sqlalchemy_con.session.query(FirmwarKeys.key_value).filter(FirmwarKeys.key_value != None).all())
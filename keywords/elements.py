import random

from locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Helpers(object):

    def send_enter(self, driver):
        driver.send_keys(Keys.ENTER)

class LoginAdminPage(object):

    def click_login_button(self, driver):
        button = driver.find_element(*AdminLoginPage_Locators.LOGINBUTTON)
        button.click()

    def input_text_to_login_field(self, driver, login):
        login_field = driver.find_element(*AdminLoginPage_Locators.USERNAME)
        login_field.send_keys(login)
        return login_field

    def input_tex_to_passwd_field(self, driver, passwd):
        passwd_field = driver.find_element(*AdminLoginPage_Locators.PASSWORD)
        passwd_field.send_keys(passwd)
        return passwd_field


class MainAdminPage(object):

    ######################################
    ######## CLICK to ANY Button #########
    ######################################

    def click_log_out_button(self, driver):
        button = driver.find_element(*AdminLoginPage_Locators.LOGOUTBUTTON)
        button.click()

    def click_save_button(self, driver):
        save_button = driver.find_element(*Buttons.SAVEBUTTTON)
        save_button.click()

    def click_save_and_continue_editing(self, driver):
        save_button = driver.find_element(*Buttons.SAVEANDCONTINUEEDITINGBUTTON)
        save_button.click()

    def click_save_and_add_another(self, driver):
        save_button = driver.find_element(*Buttons.SAVEANDADDANOTHERBUTTON)
        save_button.click()

    def click_delete_button(self, driver):
        delete_button = driver.find_element(*Buttons.DELETEBUTTON)
        delete_button.click()

    def click_to_yes_button(self, driver):
        yes = driver.find_element(*Buttons.YES)
        yes.click()

    #####################################
    ######### ALL CHECK on page #########
    #####################################

    def check_that_success(self, driver):
        try:
            driver.find_element(*AdminPage_Locators.SUCCESS)
            return 1
        except Exception as E:
            return E

    def check_that_error(self, driver):
        try:
            driver.find_element(AdminPage_Locators.SUCCESS)
            return 1
        except Exception as E:
            return E

    class Users(object):
        def click_to_users(self, driver):
            username = driver.find_element(*AdminPage_Authentification_and_Authorization_Locators.USER)
            username.click()

        def click_to_users_add(self, driver):
            add_button = driver.find_element(*AdminPage_Authentification_and_Authorization_Locators.USERADD)
            add_button.click()

        def click_to_users_change(self):
            pass

        def input_username(self, driver, username):
            username_field = driver.find_element(*AddUser.USERNAMEFIELD)
            return username_field.send_keys(username)

        def input_password(self, driver, password):
            password_field = driver.find_element(*AddUser.PASSWORDFIELD)
            return password_field.send_keys(password)

        def input_password_confirmation(self, driver, password):
            password_confirmation_field = driver.find_element(*AddUser.PASSWORDCONFIRMATIONFIELD)
            return password_confirmation_field.send_keys(password)

        def input_firstname(self, driver, firstname):
            firstname_field = driver.find_element(*AddUser.FIRSTNAMEFIELD)
            firstname_field.send_keys(firstname)

        def input_lastname(self, driver, lastname):
            lastname_field = driver.find_element(*AddUser.LASTNAMEFIELD)
            lastname_field.send_keys(lastname)

        def input_email(self, driver, email):
            email_field = driver.find_element(*AddUser.EMAILFIELAD)
            email_field.send_keys(email)

        def click_checkbox_is_active(self, driver):
            checkbox = driver.find_element(*AddUser.CHECKBOXISACTIVE)
            checkbox.click()

        def click_checckbox_is_staff(self, driver):
            checkbox = driver.find_element(*AddUser.CHECKBOSISSTAFF)
            checkbox.click()

        def click_checkbox_is_superuser(self, driver):
            checkbox = driver.find_element(*AddUser.CHECKBOXSUPERUSERSTATUS)
            checkbox.click()

        def click_to_username(self, driver, name):
            usertable = driver.find_element(*AdminPage_Authentification_and_Authorization_Locators.USERTABLE)
            username = usertable.find_element(By.LINK_TEXT, name)
            username.click()

    class Script(object):

        def click_to_script(self, driver):
            script_button = driver.find_element(*Script.SCRIPT)
            script_button.click()

        def click_to_scipt_add(self, driver):
            add_button = driver.find_element(*Script.SCRIPTADD)
            add_button.click()

        def click_to_script_change(self, driver):
            change_button = driver.find_element(*Script.SCRIPTCHANGE)
            change_button.click()

        def input_script_name(self, driver, scriptname):
            script_name_field = driver.find_element(*Script.SCRIPTNAME)
            script_name_field.send_keys(scriptname)

        def choose_os_script(self, driver, os):
            combobox = Select(driver.find_element(*Script.SCRIPTOS))
            combobox.select_by_visible_text(os)

        def input_script_file(self, driver, path):
            script_file = driver.find_element(*Script.SCRIPTFILE)
            script_file.send_keys(path)

        def click_to_script_name(self, driver, name):
            script_table = driver.find_element(*Script.SCRIPTTABLE)
            script = script_table.find_element(By.LINK_TEXT, name)
            script.click()

        def click_to_need_input_file(self, driver):
            checkbox = driver.find_element(*Script.NEEDFILE)
            checkbox.click()

    class Producgroup(object):

        def click_to_productgroup(self, driver):
            productgroup_button = driver.find_element(*Productgroup.PRODUCTGROUP)
            productgroup_button.click()

        def click_to_add_productgroup(self, driver):
            add_productgroup_button = driver.find_element(*Productgroup.PRODUCTGROUPADD)
            add_productgroup_button.click()

        def click_to_change_productgroup(self, driver):
            change_productgroup_button = driver.find_element(*Productgroup.PRODUCTGROUPCHANGE)
            change_productgroup_button.click()

        def input_producgroup_name(self, driver, name):
            name_field = driver.find_element(*Productgroup.PRODUCTGROUPNAME)
            name_field.send_keys(name)

        def click_to_prductgroup_name(self,driver, username):
            product_table = driver.find_element(*Productgroup.PRODUCTGROUPTABLE)
            row = product_table.find_element(By.LINK_TEXT, username)
            row.click()

    class Sproduct(object):

        def click_to_sproduct(self, driver):
            sproduct_button = driver.find_element(*Sproduct.SPRODUCT)
            sproduct_button.click()

        def click_to_sproduct_add(self, driver):
            add_button = driver.find_element(*Sproduct.SPRODUCTADD)
            add_button.click()

        def click_to_sproduct_change(self, driver):
            change_button = driver.find_element(*Sproduct.SPRODUCTCHANGE)
            change_button.click()

        def input_sproduct_name(self, driver, name):
            name_field = driver.find_element(*Sproduct.SPRODUCTNAME)
            name_field.send_keys(name)

        def choose_product_group(self, driver, productgroup):
            combobox = Select(driver.find_element(*Sproduct.PRODUCTGROUP))
            combobox.select_by_visible_text(productgroup)

        def choose_sign_script(self, driver, signscript):
            combobox = Select(driver.find_element(*Sproduct.SIGNSCRIPT))
            combobox.select_by_visible_text(signscript)

        def click_to_approve_needed(self, driver):
            checkbox = driver.find_element(*Sproduct.CHECKBOXAPROVENEEDED)
            checkbox.click()

        def choose_email_distribution(self,driver, username):
            combobx = Select(driver.find_element(*Sproduct.EMAILDISTRIBUTION))
            combobx.select_by_visible_text(username)

        def click_to_is_drm(self, driver):
            checkbox = driver.find_element(*Sproduct.CHECKBOXISDRM)
            checkbox.click()


    class Permission(object):

        def click_to_permission(self, driver):
            permission_button = driver.find_element(*Permission.PERMISSION)
            permission_button.click()

        def click_to_permission_add(self, driver):
            add_button = driver.find_element(*Permission.PERMISSIONADD)
            add_button.click()

        def click_to_permission_change(self, driver):
            change_button = driver.find_element(*Permission.PERMISSIONCHANGE)
            change_button.click()

        def choose_user_permission(self, driver, user):
            combobox = Select(driver.find_element(*Permission.USERCOMBOBOX))
            combobox.select_by_visible_text(user)

        def choose_product_permission(self, driver, product):
            combobox = Select(driver.find_element(*Permission.PRODUCTCOMBOBOX))
            combobox.select_by_visible_text(product)

        def click_to_approve(self, driver):
            checkbox = driver.find_element(*Permission.CHECKBOXCANAPPROVE)
            checkbox.click()

        def click_to_can_sign(self, driver):
            checkbox = driver.find_element(*Permission.CHECKBOXCASIGN)
            checkbox.click()

        def click_to_username(self, driver, username):
            perm_table = driver.find_element(*Permission.PERMISSIONTABLE)
            perm_name = perm_table.find_element(By.LINK_TEXT, username)
            perm_name.click()

        def click_to_checkbox_can_sign_on_maintable(self, driver, row):
            id = 'id_form-%D-can_sign' % row
            checkbox = driver.find_element(By.ID, id)
            checkbox.click()

        def get_text_from_selected_product(self, driver):
            combobox = Select(driver.find_element(*Permission.PRODUCTCOMBOBOX))
            a = combobox.first_selected_option()
            print a.getAttribute("textContent")
            print 1

        def click_to_permission_by_user_and_product(self, driver):
            table = driver.find_elements(*Permission.PERMISSIONTABLE)
            row = driver.find_elements


class SignPage(object):

    class Login(object):

        def input_username(self, driver, username):
            username_field = driver.find_element(*SignLogin.USERNAMEFIELD)
            username_field.send_keys(username)

        def input_password(self, driver, password):
            password_field = driver.find_element(*SignLogin.PASSWORDFIELD)
            password_field.send_keys(password)

        def click_to_login_button(self, driver):
            login_button = driver.find_element(*SignLogin.LOGINBUTTON)
            login_button.click()

        def click_to_log_out_button(self, driver):
            log_out_button = driver.find_element(*SignLogin.LOGOUT)
            log_out_button.click()

    class Sign(object):

        def click_to_sign_button(self, driver):
            sign_button = driver.find_element(*Sign.SIGNBUTTON)
            sign_button.click()

        def click_to_sign_menu(self, driver):
            sign_menu = driver.find_element(*Sign.SIGNINGMENU)
            sign_menu.click()

        def input_sign_file(self, driver, path):
            sign_file = driver.find_element(*Sign.UPLOADFILE)
            sign_file.send_keys(path)

        def choose_group(self, driver, group):
            combobox = Select(driver.find_element(*Sign.GROUPCOMBOBOX))
            combobox.select_by_visible_text(group)

        def choose_product(self, driver, product):
            combobox = Select(driver.find_element(*Sign.PROJECTCOMBOBOX))
            combobox.select_by_visible_text(product)

        def input_version(self, driver, version):
            version_field = driver.find_element(*Sign.VERSIONFIELD)
            version_field.send_keys(version)

        def input_comment(self, driver, comment):
            comment_field = driver.find_element(*Sign.COMMENTFIELD)
            comment_field.send_keys(comment)

        def input_cas_stpbbb_ids(self, driver, ids):
            casstb_field = driver.find_element(*Sign.CASSTBFIELD)
            casstb_field.send_keys(ids)

        def choose_date_from_month(self, driver, month):
            combobox = Select(driver.find_element(*Sign.DATEFROMMONTH))
            combobox.select_by_visible_text(month)

        def choose_date_from_day(self, driver, day):
            combobox = Select(driver.find_element(*Sign.DATEFROMDAY))
            combobox.select_by_visible_text(day)

        def choose_date_from_year(self, driver, year):
            combobox = Select(driver.find_element(*Sign.DATEFROMYEAR))
            combobox.select_by_visible_text(year)

        def choose_date_to_month(self, driver, month):
            combobox = Select(driver.find_element(*Sign.DATETOMONTH))
            combobox.select_by_visible_text(month)

        def choose_date_to_day(self, driver, day):
            combobox = Select(driver.find_element(*Sign.DATETODAY))
            combobox.select_by_visible_text(day)

        def choose_date_to_year(self, driver, year):
            combobox = Select(driver.find_element(*Sign.DATETOYEAR))
            combobox.select_by_visible_text(year)

class HystoryPage(object):

    def get_table_like_list_tuples(self, driver):
        list_table = []
        table = driver.find_element(*Hystory.HYSTORYTABLE)
        for row in table.find_elements_by_tag_name('tr'):
            if row.text.startswith('#') != True:
                cells = row.find_elements_by_tag_name('td')
                list_table.append((cells[1].text, cells[2].text, cells[3].text,cells[4].text, cells[5].text))
        return list_table


    def click_to_first_log(self, driver):
        log_button = driver.find_element(*Hystory.FIRSTLOG)
        log_button.click()

    def get_script_status(self, driver):
        status = driver.find_element(*Hystory.STATUS)
        return status.text

    def click_to_first_sign_again(self, driver):
        sign_again = driver.find_element(*Hystory.FIRSTRESIGN)
        sign_again.click()

    def choose_sort_type(self, driver, type):
        combobox = Select(driver.find_element(*Hystory.SORTTYPE))
        combobox.select_by_visible_text(type)

    def get_hystory_table_after_filter(self, driver):
        dict_filter = {}
        table = driver.find_element(*Hystory.HYSTORYTABLE)
        for row in table.find_elements_by_tag_name('tr'):
            if row.text.startswith('#') != True:
                cells = row.find_elements_by_tag_name('td')
                dict_filter[cells[1].text] = cells[6].text[:-21]
        return dict_filter

    def input_comment_in_random_row(self, driver, comment):
        table = driver.find_element(*Hystory.HYSTORYTABLE)
        table_rows = table.find_elements_by_tag_name('tr')
        row_in_table = random.randint(1, (len(table_rows) -1))
        headers = table_rows[0]
        cells = headers.find_elements_by_tag_name('th')
        index_comment = 1
        for cell in cells:
            if cell.text == 'Additional':
                break
            index_comment +=1
        table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]/div' % (row_in_table + 1, index_comment)).clear()
        table.find_element_by_xpath('.//tbody/tr[%s]/td[%s]/div' % (row_in_table + 1, index_comment)).send_keys(comment)
        driver.find_element_by_link_text('#').click()

    def click_to_sort_by_comment(self, driver):
        button = driver.find_element(*Hystory.SORTBUTTONCOMMENT)
        button.click()

    def click_to_sort_by_filename(self, driver):
        button = driver.find_element(*Hystory.SORTBUTTONFILENAME)
        button.click()

    def click_to_sort_by_project(self, driver):
        button = driver.find_element(*Hystory.SORTBUTTONPROJECT)
        button.click()

    def click_to_sort_by_version(self, driver):
        button = driver.find_element(*Hystory.SORTBUTTONVERSION)
        button.click()


class ApprovePage(object):

    def click_to_approval_page(self, driver):
        approval = driver.find_element(*Approve.APPROVEPAGE)
        approval.click()

    def click_to_first_approve_button(self, driver):
        approve_button = driver.find_element(*Approve.FIRSTAPPROVE)
        approve_button.click()

    def click_to_first_refuse_button(self, driver):
        refuse_button = driver.find_element(*Approve.FIRSTREFUSE)
        refuse_button.click()

    def choose_sort_type(self, driver, type):
        combobox = Select(driver.find_element(*Approve.SORTTYPE))
        combobox.select_by_visible_text(type)
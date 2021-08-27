from locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Logger import log
import elements as elem
import time
from datetime import datetime



class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver):
        self.driver = driver

class SearchTextElement(BasePage):
    """This class gets the search text from the specified locator"""
    def wait_until_page_load(self, element_locator, time=0.1):
        try:
            WebDriverWait(self.driver, time).until(lambda driver: driver.find_element(*element_locator))
            return 1
        except Exception as E:
            log(E)
            return E

class LoginPage(BasePage):
    """Base class to initialize the base page that will be called from all pages"""
    def input_admin_login_password(self, login, password):
        assert (SearchTextElement(self.driver).wait_until_page_load(AdminLoginPage_Locators.USERNAME) == 1), "Page Login to administrator not loaded"
        elem.LoginAdminPage().input_text_to_login_field(self.driver, login)
        return elem.LoginAdminPage().input_tex_to_passwd_field(self.driver, password)


    def click_login_button(self):
        elem.LoginAdminPage().click_login_button(self.driver)
        assert (SearchTextElement(self.driver).wait_until_page_load(AdminPage_Locators.ALLPAGE) == 1), "Login was not correct"

    def push_enter(self, any_field, signpage = False):
        elem.Helpers().send_enter(any_field)
        if signpage is False:
            assert (SearchTextElement(self.driver).wait_until_page_load(AdminPage_Locators.ALLPAGE) == 1), "Login to admin panel was not correct"
        else:
            assert (SearchTextElement(self.driver).wait_until_page_load(Sign.SIGNINGMENU) == 1), "Login to signing was not correct"


    def admin_logout(self):
         elem.MainAdminPage().click_log_out_button(self.driver)
         assert (SearchTextElement(self.driver).wait_until_page_load(AdminLoginPage_Locators.LOGGEDOUT) == 1), "Log OUT was not correct"

    def sign_input_username_password(self, username, password):
        assert (SearchTextElement(self.driver).wait_until_page_load(SignLogin.USERNAMEFIELD) == 1), "Page Sign not loaded"
        elem.SignPage().Login().input_username(self.driver, username)
        return elem.SignPage().Login().input_password(self.driver, password)

    def sign_click_to_login_button(self):
        elem.SignPage().Login().click_to_login_button(self.driver)

    def sign_click_to_logout_button(self):
        elem.SignPage().Login().click_to_log_out_button(self.driver)

class AdminPage(BasePage):

    def check_that_somethink_was_added(self, time=0.1):
        assert (SearchTextElement(self.driver).wait_until_page_load(AdminPage_Locators.SUCCESS, time) == 1), "SOMETHING was not added correct"

    def user_click_user_button(self):
        elem.MainAdminPage().Users().click_to_users(self.driver)

    def click_to_user_add_button(self):
        elem.MainAdminPage().Users().click_to_users_add(self.driver)

    def add_new_user(self, username, password):
        if password is None:
            return elem.MainAdminPage().Users().input_username(self.driver, username)
        else:
            elem.MainAdminPage().Users().input_username(self.driver, username)
        elem.MainAdminPage().Users().input_password(self.driver, password)
        if password == 'different':
            return elem.MainAdminPage().Users().input_password_confirmation(self.driver, password + 'password')
        else:
            return elem.MainAdminPage().Users().input_password_confirmation(self.driver, password)

    def click_any_save_button_or_delete(self, name_button):
        if name_button == 'save':
            elem.MainAdminPage().click_save_button(self.driver)
        elif name_button == 'save_and_continue':
            elem.MainAdminPage().click_save_and_continue_editing(self.driver)
        elif name_button == 'save_and_add_another':
            elem.MainAdminPage().click_save_and_add_another(self.driver)
        elif name_button == 'delete':
            elem.MainAdminPage().click_delete_button(self.driver)

    def click_to_yes_button(self):
        elem.MainAdminPage().click_to_yes_button(self.driver)

    def user_click_to_username(self, name):
        elem.MainAdminPage().Users().click_to_username(self.driver, name)

    def click_any_checkbox_in_add_user(self, checkbox_name):
        if checkbox_name == 'is_active':
            elem.MainAdminPage().Users().click_checkbox_is_active(self.driver)
        elif checkbox_name == 'is_staff':
            elem.MainAdminPage().Users().click_checckbox_is_staff(self.driver)
        elif checkbox_name == 'is_superuser':
            elem.MainAdminPage().Users().click_checkbox_is_superuser(self.driver)

    ################################################################
    ############# SCRIPTS
    ################################################################

    def script_click_to_add_button(self):
        elem.MainAdminPage().Script().click_to_scipt_add(self.driver)

    def script_choose_os(self, os):
        elem.MainAdminPage().Script().choose_os_script(self.driver, os)

    def script_input_new_file(self, path):
        elem.MainAdminPage().Script().input_script_file(self.driver, path)

    def script_input_scriptname(self, name):
        if name == 'empty':
            pass
        else:
            elem.MainAdminPage().Script().input_script_name(self.driver, name)

    def script_click_to_signscript_button(self):
        elem.MainAdminPage().Script().click_to_script(self.driver)

    def script_click_need_input_file(self, status):
        if status == 'enable':
            pass
        else:
            elem.MainAdminPage().Script().click_to_need_input_file(self.driver)


    ################################################################
    ############# Productgroup
    ################################################################

    def productgroup_click_to_add_button(self):
        elem.MainAdminPage().Producgroup().click_to_add_productgroup(self.driver)

    def productgroup_click_to_productgroup_button(self):
        elem.MainAdminPage().Producgroup().click_to_productgroup(self.driver)

    def productgroup_click_to_change(self):
        elem.MainAdminPage().Producgroup().click_to_change_productgroup(self.driver)

    def productgroup_input_name(self, name):
        if name == 'empty':
            pass
        else:
            elem.MainAdminPage().Producgroup().input_producgroup_name(self.driver, name)

    def productgroup_click_to_prductgroup_name(self, username):
        elem.MainAdminPage().Producgroup().click_to_prductgroup_name(self.driver, username)

    ################################################################
    ############# Sproduct
    ################################################################

    def sproduct_click_to_sproduct_button(self):
        elem.MainAdminPage().Sproduct().click_to_sproduct(self.driver)

    def sproduct_click_to_add_button(self):
        elem.MainAdminPage().Sproduct().click_to_sproduct_add(self.driver)

    def sproduct_click_to_change_button(self):
        elem.MainAdminPage().Sproduct().click_to_sproduct_change(self.driver)

    def sproduct_input_name(self, name):
        if name == 'empty':
            pass
        else:
            elem.MainAdminPage().Sproduct().input_sproduct_name(self.driver, name)

    def sproduct_choose_product_group(self, name):
        elem.MainAdminPage().Sproduct().choose_product_group(self.driver, name)

    def sproduct_choose_signscript(self, name):
        elem.MainAdminPage().Sproduct().choose_sign_script(self.driver, name)

    def sproduct_approve_needed(self, approve):
        if approve == 'True':
            pass
        else:
            elem.MainAdminPage().Sproduct().click_to_approve_needed(self.driver)

    def sproduct_is_drm(self, drm):
        if drm == 'True':
            elem.MainAdminPage().Sproduct().click_to_is_drm(self.driver)
        else:
            pass

    def sproduct_choose_email_distribution(self, name):
        if name == 'empty':
            pass
        else:
            elem.MainAdminPage().Sproduct().choose_email_distribution(self.driver, name)

    ################################################################
    ############# Permission
    ################################################################

    def permission_click_to_permission_button(self):
        elem.MainAdminPage().Permission().click_to_permission(self.driver)

    def permission_click_to_add_button(self):
        elem.MainAdminPage().Permission().click_to_permission_add(self.driver)

    def permission_click_to_change_button(self):
        elem.MainAdminPage().Permission().click_to_permission_change(self.driver)

    def permission_choose_user(self, name):
        elem.MainAdminPage().Permission().choose_user_permission(self.driver, name)

    def permission_choose_product(self, name):
        elem.MainAdminPage().Permission().choose_product_permission(self.driver, name)

    def permission_can_approve(self, approve):
        if approve == 'True':
            elem.MainAdminPage().Permission().click_to_approve(self.driver)
        else:
            pass

    def permission_can_sign(self, cansign):
        if cansign == 'True':
            elem.MainAdminPage().Permission().click_to_can_sign(self.driver)
        else:
            pass

    def permission_click_to_username(self, username):
        elem.MainAdminPage().Permission().click_to_username(self.driver, username)

    def permission_get_text_from_field_product(self):
        elem.MainAdminPage().Permission().get_text_from_selected_product(self.driver)


    def change_permission(self, name):
        elem.MainAdminPage().Permission().click_to_permission_change(self.driver)
        elem.MainAdminPage().Permission().click_to_username(self.driver, name)

class SigningPage(BasePage):

    def check_that_file_was_signed(self, time=0.1):
        assert (SearchTextElement(self.driver).wait_until_page_load(Hystory.HYSTORYTABLE, time) == 1), "FILE was not signed correct"

    def sign_upload_file(self, filepath):
        if filepath == 'empty':
            pass
        else:
            elem.SignPage().Sign().input_sign_file(self.driver, filepath)

    def sign_go_to_sign_page(self):
        elem.SignPage().Sign().click_to_sign_menu(self.driver)

    def sign_click_to_sign_button(self):
        elem.SignPage().Sign().click_to_sign_button(self.driver)

    def sign_choose_group(self, group):
        elem.SignPage().Sign().choose_group(self.driver, group)

    def sign_choose_product(self, product):
        elem.SignPage().Sign().choose_product(self.driver, product)

    def sign_input_version(self, version):
        if version == 'False':
            pass
        else:
            elem.SignPage().Sign().input_version(self.driver, version)

    def sign_input_comment(self, comment):
        if comment == 'empty':
            pass
        else:
            elem.SignPage().Sign().input_comment(self.driver, comment)

    def sign_input_cas_stb_ids(self, ids):
        elem.SignPage().Sign().input_cas_stpbbb_ids(self.driver, ids)

    def sign_choose_date_from_month(self, month):
        elem.SignPage().Sign().choose_date_from_month(self.driver, month)

    def sign_choose_date_from_day(self, day):
        elem.SignPage().Sign().choose_date_from_month(self.driver, day)

    def sign_choose_date_from_year(self, year):
        elem.SignPage().Sign().choose_date_from_year(self.driver, year)

    def sign_choose_date_to_month(self, month):
        elem.SignPage().Sign().choose_date_to_month(self.driver, month)

    def sign_choose_date_to_day(self, day):
        elem.SignPage().Sign().choose_date_to_day(self.driver, day)

    def sign_choose_date_to_year(self, year):
        elem.SignPage().Sign().choose_date_to_year(self.driver, year)

class HystoryPage(BasePage):

    def get_table_like_list_tuples(self):
        return elem.HystoryPage().get_table_like_list_tuples(self.driver)

    def click_to_first_log(self):
        elem.HystoryPage().click_to_first_log(self.driver)

    def check_that_script_ready(self):
        t1 = datetime.now()
        while (datetime.now() - t1).seconds <= 15:
            time.sleep(0.5)
            status = elem.HystoryPage().get_script_status(self.driver)
            if status == 'Status: ready':
                return 1
            elif status == 'Status: fail':
                return 0
        return 0

    def click_to_resign(self):
        elem.HystoryPage().click_to_first_sign_again(self.driver)

    def choose_filter_on_page(self, status):
        elem.HystoryPage().choose_sort_type(self.driver, status)

    def get_table_elem_after_filter(self):
        return elem.HystoryPage().get_hystory_table_after_filter(self.driver)

    def change_comment(self, comment):
        elem.HystoryPage().input_comment_in_random_row(self.driver, comment)

    def check_sort_in_history(self, type_to_sort):
        if type_to_sort == "Additional":
            elem.HystoryPage().click_to_sort_by_comment(self.driver)
        elif type_to_sort == "File name":
            elem.HystoryPage().click_to_sort_by_filename(self.driver)
        elif type_to_sort == "Project":
            elem.HystoryPage().click_to_sort_by_project(self.driver)
        elif type_to_sort == "Version":
            elem.HystoryPage().click_to_sort_by_version(self.driver)
        else:
            return 'Please choose correct type to sort'

class ApprovePage(BasePage):

    def click_to_approve_page(self, type):
        if type == 'True' or type == 'Refuse':
            elem.ApprovePage().click_to_approval_page(self.driver)
        else:
            pass


    def click_to_first_approve_or_refuse_button(self, type):
        if type == 'True':
            elem.ApprovePage().click_to_first_approve_button(self.driver)
        elif type == 'Refuse':
            elem.ApprovePage().click_to_first_refuse_button(self.driver)
        else:
            pass

    def choose_filter_on_page(self, status):
        elem.ApprovePage().choose_sort_type(self.driver, status)


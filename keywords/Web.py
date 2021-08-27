from selenium.webdriver import Chrome
import page
from Logger import log


driver = Chrome()

def login(login='stp', password='1', button = False):
    driver.get('https://127.0.0.1/admin')
    login_page = page.LoginPage(driver)
    password_field = login_page.input_admin_login_password(login, password)
    if button:
        login_page.push_enter(password_field)
    else:
        login_page.click_login_button()


def __logout(sign=False):
    if sign:
        log_out = page.LoginPage(driver)
        log_out.sign_click_to_logout_button()
    else:
        log_out = page.LoginPage(driver)
        log_out.admin_logout()

def login_to_sign(login='stp', password='1', button = False):
    driver.get('https://127.0.0.1')
    login_page = page.LoginPage(driver)
    password_field = login_page.sign_input_username_password(login, password)
    if button:
        login_page.push_enter(password_field, True)
    else:
        login_page.sign_click_to_login_button()



def adding_new_users(username, password=None):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.click_to_user_add_button()
        admin_page.add_new_user(username, password)
        admin_page.click_any_save_button_or_delete('save')
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except:
        __logout()
        return 0

def add_new_script(name, path, os='Debian8', need_file='enable'):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.script_click_to_add_button()
        admin_page.script_input_new_file(path)
        admin_page.script_choose_os(os)
        admin_page.script_input_scriptname(name)
        admin_page.script_click_need_input_file(need_file)
        admin_page.click_any_save_button_or_delete('save')
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        log(E)
        __logout()
        return 0

def add_new_productgroup(name):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.productgroup_click_to_add_button()
        admin_page.productgroup_input_name(name)
        admin_page.click_any_save_button_or_delete('save')
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        log(E)
        __logout()
        return 0


def add_new_sproduct(sproductname, productgroup, signscript, approve, email, drm):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.sproduct_click_to_add_button()
        admin_page.sproduct_input_name(sproductname)
        admin_page.sproduct_choose_product_group(productgroup)
        admin_page.sproduct_choose_signscript(signscript)
        admin_page.sproduct_approve_needed(approve)
        admin_page.sproduct_is_drm(drm)
        admin_page.sproduct_choose_email_distribution(email)
        admin_page.click_any_save_button_or_delete('save')
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        log(E)
        __logout()
        return 0



def add_new_permission(user, product, approve, cansign='True'):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.permission_click_to_add_button()
        admin_page.permission_choose_user(user)
        admin_page.permission_choose_product(product)
        admin_page.permission_can_approve(approve)
        admin_page.permission_can_sign(cansign)
        admin_page.click_any_save_button_or_delete('save')
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        log(E)
        __logout()
        return 0

def edit_permission(user, approve, cansign, newuser="False", product="False"):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.permission_click_to_change_button()
        admin_page.permission_click_to_username(user)
        admin_page.permission_get_text_from_field_product()
        if newuser != "False":
            admin_page.permission_choose_user(user)
        if product != "False":
            admin_page.permission_choose_product(product)
        admin_page.permission_can_approve(approve)
        admin_page.permission_can_sign(cansign)
        admin_page.click_any_save_button_or_delete('save')
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        log(E)
        __logout()
        return 0

def sign_without_drm_and_check_that_signed(filepath, groupe, product, comment, login, password, version='False', approve = 'True'):
    try:
        login_to_sign(login, password)
        sign_page = page.SigningPage(driver)
        sign_page.sign_go_to_sign_page()
        sign_page.sign_upload_file(filepath)
        sign_page.sign_choose_group(groupe)
        sign_page.sign_choose_product(product)
        sign_page.sign_input_comment(comment)
        sign_page.sign_input_version(version)
        sign_page.sign_click_to_sign_button()
        sign_page.check_that_file_was_signed()
        hystory_page = page.HystoryPage(driver)
        hystory_page.click_to_first_log()
        assert (hystory_page.check_that_script_ready() == 1), 'Script not ready'
        approve_page = page.ApprovePage(driver)
        approve_page.click_to_approve_page(approve)
        approve_page.click_to_first_approve_or_refuse_button(approve)
        __logout(sign=True)
        return 1
    except Exception as E:
        log(E)
        __logout(sign=True)
        return 0

def sign_again(filepath, login, password):
    try:
        login_to_sign(login, password)
        hystory_page = page.HystoryPage(driver)
        hystory_page.click_to_resign()
        sign_page = page.SigningPage(driver)
        sign_page.sign_upload_file(filepath)
        sign_page.sign_click_to_sign_button()
        hystory_page.click_to_first_log()
        assert (hystory_page.check_that_script_ready() == 1), 'Script not ready'
        __logout(sign=True)
        return 1
    except Exception as E:
        log(E)
        __logout(sign=True)
        return 0

def sign_again_and_change_parametr(filepath, groupe, product, comment, login, password, version='False'):
    try:
        login_to_sign(login, password)
        hystory_page = page.HystoryPage(driver)
        hystory_page.click_to_resign()
        sign_page = page.SigningPage(driver)
        sign_page.sign_upload_file(filepath)
        sign_page.sign_choose_group(groupe)
        sign_page.sign_choose_product(product)
        sign_page.sign_input_comment(comment)
        sign_page.sign_input_version(version)
        sign_page.sign_click_to_sign_button()
        hystory_page.click_to_first_log()
        assert (hystory_page.check_that_script_ready() == 1), 'Script not ready'
        __logout(sign=True)
        return 1
    except Exception as E:
        __logout(sign=True)
        log(E)
        return 0

def check_filter_history_web(status):
    try:
        login_to_sign()
        hystory_page = page.HystoryPage(driver)
        hystory_page.choose_filter_on_page(status)
        dict_from_site = hystory_page.get_table_like_list_tuples()
        __logout(sign=True)
        return dict_from_site
    except Exception as E:
        __logout(sign=True)
        log(E)
        return 0

def check_filter_approve_web(status):
    try:
        login_to_sign()
        approve_page = page.ApprovePage(driver)
        approve_page.click_to_approve_page('True')
        approve_page.choose_filter_on_page(status)
        hystory_page = page.HystoryPage(driver)
        dict_from_site = hystory_page.get_table_like_list_tuples()
        __logout(sign=True)
        return dict_from_site
    except Exception as E:
        __logout(sign=True)
        log(E)
        return 0

def change_comment_web(comment):
    try:
        login_to_sign()
        hystory_page = page.HystoryPage(driver)
        hystory_page.change_comment(comment)
        __logout(sign=True)
        return 1
    except Exception as E:
        __logout(sign=True)
        log(E)
        return 0

def check_sort_in_history_web(type_to_sort, approve=False):
    try:
        login_to_sign()
        if approve is not False:
            approve_page = page.ApprovePage(driver)
            approve_page.click_to_approve_page(approve)
        hystory_page = page.HystoryPage(driver)
        hystory_page.check_sort_in_history(type_to_sort)
        table_from_site = hystory_page.get_table_like_list_tuples()
        __logout(sign=True)
        return table_from_site
    except Exception as E:
        __logout(sign=True)
        log(E)
        return 0

def delete_permission(name):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.permission_click_to_permission_button()
        admin_page.permission_click_to_username(name)
        admin_page.click_any_save_button_or_delete('delete')
        admin_page.click_to_yes_button()
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        __logout()
        log(E)
        return 0

def delete_one_productgroup(name):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.productgroup_click_to_productgroup_button()
        admin_page.productgroup_click_to_prductgroup_name(name)
        admin_page.click_any_save_button_or_delete('delete')
        admin_page.click_to_yes_button()
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        __logout()
        log(E)
        return 0

def delete_one_signscript(name):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.script_click_to_signscript_button()
        admin_page.productgroup_click_to_prductgroup_name(name)
        admin_page.click_any_save_button_or_delete('delete')
        admin_page.click_to_yes_button()
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        __logout()
        log(E)
        return 0

def delete_one_user(name):
    try:
        login()
        admin_page = page.AdminPage(driver)
        admin_page.user_click_user_button()
        admin_page.user_click_to_username(name)
        admin_page.click_any_save_button_or_delete('delete')
        admin_page.click_to_yes_button()
        admin_page.check_that_somethink_was_added()
        __logout()
        return 1
    except Exception as E:
        __logout()
        log(E)
        return 0
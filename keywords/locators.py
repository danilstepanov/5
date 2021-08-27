from selenium.webdriver.common.by import By

class AdminLoginPage_Locators(object):
    LOGINBUTTON = (By.XPATH, '//*[@id="login-form"]/div[3]/input')
    USERNAME = (By.ID, 'id_username')
    PASSWORD = (By.ID, 'id_password')
    LOGOUTBUTTON = (By.XPATH, '//*[@id="user-tools"]/a[3]')
    LOGGEDOUT = (By.CLASS_NAME, 'colM')
    LOGINAGAIN = (By.XPATH, '//*[@id="content"]/p[2]/a')

class AdminPage_Locators(object):
    ALLPAGE = (By.ID, 'content')
    MAINPERMISSION = (By.CLASS_NAME, 'model-permission')
    SUCCESS = (By.CLASS_NAME, 'success')
    ERROR = ()

class AdminPage_Authentification_and_Authorization_Locators(object):
    USER = (By.XPATH, '//*[@id="content-main"]/div[1]/table/tbody/tr/th/a')
    USERADD = (By.XPATH, '//*[@id="content-main"]/div[1]/table/tbody/tr/td[1]/a')
    USERCHANGE = (By.XPATH, '//*[@id="content-main"]/div[1]/table/tbody/tr/td[2]/a')
    USERTABLE = (By.ID, 'result_list')

class Buttons(object):
    SAVEBUTTTON = (By.NAME, '_save')
    SAVEANDADDANOTHERBUTTON = (By.NAME, '_addanother')
    SAVEANDCONTINUEEDITINGBUTTON = (By.NAME, '_continue')
    DELETEBUTTON = (By.LINK_TEXT, 'Delete')
    YES = (By.XPATH, '//*[@id="content"]/form/div/input[2]')

class AddUser(object):
    USERNAMEFIELD = (By.ID, 'id_username')
    PASSWORDFIELD = (By.ID, 'id_password1')
    PASSWORDCONFIRMATIONFIELD = (By.ID, 'id_password2')
    FIRSTNAMEFIELD = (By.ID, 'id_first_name')
    LASTNAMEFIELD = (By.ID, 'id_last_name')
    EMAILFIELAD = (By.ID, 'id_email')
    CHECKBOXISACTIVE = (By.ID, 'id_is_active')
    CHECKBOSISSTAFF = (By.ID, 'id_is_staff')
    CHECKBOXSUPERUSERSTATUS = (By.ID, 'id_is_superuser')

class Script(object):
    SCRIPT = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[3]/th/a')
    SCRIPTADD = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[3]/td[1]/a')
    SCRIPTCHANGE = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[4]/td[2]/a')
    SCRIPTFILE = (By.ID, 'id_script_zip')
    SCRIPTNAME = (By.ID, 'id_name')
    SCRIPTOS = (By.ID, 'id_target_os')
    SCRIPTTABLE = (By.ID, 'result_list')
    NEEDFILE = (By.NAME, 'need_input_file')

class Productgroup(object):
    PRODUCTGROUP = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/th/a')
    PRODUCTGROUPADD = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/td[1]/a')
    PRODUCTGROUPCHANGE = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/td[2]/a')
    PRODUCTGROUPNAME = (By.ID, 'id_name')
    PRODUCTGROUPTABLE = (By.ID, 'result_list')

class Sproduct(object):
    SPRODUCT = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[4]/th/a')
    SPRODUCTADD = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[4]/td[1]/a')
    SPRODUCTCHANGE = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[4]/td[2]/a')
    SPRODUCTNAME = (By.ID, 'id_name')
    PRODUCTGROUP = (By.ID, 'id_product_group')
    SIGNSCRIPT = (By.ID, 'id_sign_script')
    CHECKBOXAPROVENEEDED = (By.ID, 'id_aprove_needed')
    EMAILDISTRIBUTION = (By.ID, 'id_emails')
    CHECKBOXISDRM = (By.ID, 'id_is_drm')

class Permission(object):
    PERMISSION = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a')
    PERMISSIONADD = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a')
    PERMISSIONCHANGE = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[2]/a')
    PERMISSIONTABLE = (By.ID, 'result_list')
    USERCOMBOBOX = (By.ID, 'id_user')
    PRODUCTCOMBOBOX = (By.ID, 'id_product')
    CHECKBOXCANAPPROVE = (By.ID, 'id_can_approve')
    CHECKBOXCASIGN = (By.ID, 'id_can_sign')

class SignLogin(object):
    USERNAMEFIELD = (By.ID, 'id_username')
    PASSWORDFIELD = (By.ID, 'id_password')
    LOGINBUTTON = (By.CLASS_NAME, 'ico_L_ready')
    LOGOUT = (By.CLASS_NAME, 'ico_baseExit')

class Sign(object):
    SIGNINGMENU = (By.CLASS_NAME, 'ico_menuSigning')
    UPLOADFILE = (By.ID, 'id_file_for_sign')
    GROUPCOMBOBOX = (By.ID, 'id_project_group')
    PROJECTCOMBOBOX = (By.ID, 'id_project')
    VERSIONFIELD = (By.ID, 'id_version_field')
    COMMENTFIELD = (By.ID, 'id_comment')
    CASSTBFIELD = (By.ID, 'id_casstbids')
    DATEFROMMONTH = (By.ID, 'id_date_from_month')
    DATEFROMDAY = (By.ID, 'id_date_from_day')
    DATEFROMYEAR = (By.ID, 'id_date_from_year')
    DATETOMONTH = (By.ID, 'id_date_to_month')
    DATETODAY = (By.ID, 'id_date_to_day')
    DATETOYEAR = (By.ID, 'id_date_to_year')
    SIGNBUTTON = (By.CLASS_NAME, 'ico_L_ready')

class Hystory(object):
    HYSTORYTABLE = (By.CLASS_NAME, 'maintable')
    FIRSTLOG = (By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr[2]/td[5]/a[1]')
    STATUS = (By.ID, 'status')
    #FIRSTRESIGN = (By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr[2]/td[9]/a')
    FIRSTRESIGN = (By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr[2]/td[5]/a')
    SORTTYPE = (By.NAME, 'sort_type_history')
    SORTBUTTONCOMMENT = (By.LINK_TEXT, 'Additional')
    SORTBUTTONFILENAME = (By.LINK_TEXT, 'File')
    SORTBUTTONPROJECT = (By.LINK_TEXT, 'Product')

class Approve(object):
    APPROVEPAGE = (By.CLASS_NAME, 'ico_menuApproval')
    APPROVETABLE = (By.CLASS_NAME, 'maintable')
    FIRSTAPPROVE = (By.XPATH, '//*[@id="content"]/div/div[2]/table/tbody/tr[2]/td[6]/div/form/button[1]')
    FIRSTREFUSE = (By.ID, 'refuse1')
    SORTTYPE = (By.NAME, 'sort_type_approval')
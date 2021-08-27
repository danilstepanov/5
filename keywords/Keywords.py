import random
from Logger import log
import Database as DB
import ssrv_helper as ssrv
import check_db
import checking_mail

class Keywords(object):

    def __init__(self):
        self.db = DB.Database()
        log('__init__ Success')

    def get_random_int(self, a, b):
        return random.randint(int(a), int(b))

    def sum(self, arg1, arg2):
        return int(arg1) + int(arg2)

    def create_my_list(self, start, end, full_range=1):
        if full_range == 1:
            li = list(range(int(start), int(end) + 1))
        else:
            li = list(range(int(start), int(end), 2))
        log('create_my_list return %s' % li)
        return li

    def get_number_rows_from_table(self, table_name):
        log('=====get_number_rows_from_table from table %s START=====' % table_name)
        if table_name == 'auth_group':
            return check_db.get_number_group(self.db)
        if table_name == 'auth_permission':
            return check_db.get_number_permission(self.db)
        if table_name == 'auth_user':
            return check_db.get_number_user(self.db)
        if table_name == 'auth_user_groups':
            return check_db.get_number_user_groups(self.db)
        if table_name == 'auth_user_user_permissions':
            return check_db.get_number_user_user_permission(self.db)
        if table_name == 'signserver_permission':
            return check_db.get_number_signserver_permission(self.db)
        if table_name == 'signserver_productgroup':
            return check_db.get_number_signserver_productgroup(self.db)
        if table_name == 'signserver_signscript':
            return check_db.get_number_signserver_signscript(self.db)
        if table_name == 'signserver_sproduct':
            return check_db.get_number_signserver_sproduct(self.db)
        if table_name == 'signserver_sproduct_emails':
            return check_db.get_number_signserver_sproduct_email(self.db)
        if table_name == 'signserver_signfile':
            return check_db.get_number_signserver_sign_file(self.db)

    def post_signing(self, sign_file, user, paswd):
        log('=====Post_signing START====')
        return check_db.post_signing(self.db, sign_file, user, paswd, download=None, drm=None)

    def post_signing_and_download(self, sign_file, user, paswd):
        log('====Post sign for downlad START====')
        return check_db.post_signing(self.db, sign_file, user, paswd, download=1, drm=None)

    def post_signing_drm_and_download(self, sign_file, user, passwd):
        log('====Post sign for drm project and download====')
        return check_db.post_signing(self.db, sign_file, user, passwd, download=1, drm=True)

    def check_db_script(self, name):
        log('=====check_db_after_adding_script START====')
        return check_db.check_db_script(self.db, name)

    def check_db_productgroup(self, name):
        log('====check_db_after_adding_productgroup START=====')
        return check_db.check_db_productgroup(self.db, name)

    def check_db_sproduct(self, name, status):
        log('=====check_db_after_adding_sproduct START====')
        return check_db.check_db_sproduct(self.db, str(name), status)

    def check_db_permission(self, username, sproduct, status):
        log('====check_db_after_adding_permission START====')
        return check_db.check_db_permission(self.db, username, sproduct, status)

    def check_db_userinfo(self, username, firstname, lastname, email):
        log('====check_userinfo_in_db START====')
        return check_db.check_db_userinfo(self.db, username, firstname, lastname, email)

    def check_filter_approve(self, status, dict_web):
        log('====check_filter_approve START====')
        return check_db.check_filter_history(self.db, status, dict_web)

    def check_filter_history(self, status, dict_web):
        log('====check_filter_history START====')
        return check_db.check_filter_history(self.db, status, dict_web)

    def check_added_user(self, username):
        log('====check added user START====')
        return check_db.check_added_user(self.db, str(username))

    def get_any_productgroup(self):
        log('====get any productgroup START====')
        return check_db.get_any_productgroup(self.db)

    def get_any_user(self):
        log('====get_any_user START====')
        return check_db.get_any_user(self.db)

    def get_any_superuser(self):
        log('====get any superuser START====')
        return check_db.get_any_superuser(self.db)

    def get_any_sproduct(self):
        log('get_any_sproduct START====')
        return check_db.get_any_sproduct(self.db)

    def get_any_signscript(self):
        log('====get_any_signscript START====')
        return check_db.get_any_signscript(self.db)

    def get_any_permission_id(self):
        log('====get_any_permission START====')
        return check_db.get_any_permission_id(self.db)

    def get_any_username_with_permission(self):
        log('====get_any_username_with_permission START====')
        return check_db.get_any_username_with_permission(self.db)

    def get_sproduct_by_permission_id(self, permisssion_id):
        log('====get sproduct by permission id START====')
        return check_db.get_sproduct_by_permission_id(self.db, permisssion_id)

    def get_username_by_permission_id(self, permission_id):
        log('====get_username_by_permission_id START====')
        return check_db.get_username_by_permission_id(self.db, permission_id)

    def get_any_username_for_permission_without_can_sign_can_approve(self):
        log('====get_any_username_for_permission_without_can_sign_can_approve START====')
        perm_id = check_db.get_any_permission_id_without_sign_and_approve(self.db)
        return check_db.get_username_by_permission_id(self.db, perm_id)

    def get_permission_status_by_permission_id(self, permission_id):
        log('====get_permission_status_by_permission_id START====')
        return check_db.get_permission_status_by_permission_id(self.db, permission_id)

    def get_username_without_permission(self):
        log('get_user_id_without_permission')
        return check_db.get_username_without_permission(self.db)

    def check_email(self, user, product, letters):
        log('====check email START====')
        return checking_mail.check_email(str(user), str(product), int(letters))

    def clean_email(self):
        log('====clean email START====')
        return checking_mail.clean_email()

    def check_empty_email(self):
        log('====checking empty email START====')
        return checking_mail.check_email(user=None, product=None, letters=0)

    def get_product_last_signing(self):
        log('====get product last signing START====')
        return check_db.get_project_last_signing(self.db)

    def check_sort_by_project(self,table_from_site):
        log('====Check sort by project START====')
        return check_db.check_sort_in_history(self.db,table_from_site, type_to_sort='Project')

    def check_sort_by_file_name(self,table_from_site):
        log('====check sort by file name====')
        return check_db.check_sort_in_history(self.db,table_from_site, type_to_sort='blank_file')

    def check_sort_by_comment(self, table_from_site):
        log('====check sort by comment START====')
        return check_db.check_sort_in_history(self.db, table_from_site, type_to_sort='comment')

    def check_sort_by_version(self,table_from_site):
        log('====check sort by version START====')
        return check_db.check_sort_in_history(self.db,table_from_site, type_to_sort='Version')

    def check_sort_by_file_name_in_approval(self,table_from_site):
        log('====check sort by filename in approval START====')
        return check_db.check_sort_in_approval(self.db,table_from_site, type_to_sort='File name')

    def check_sort_by_project_in_approval(self,table_from_site):
        log('====check sort by project in approval START====')
        return check_db.check_sort_in_approval(self.db,table_from_site, type_to_sort='Project')

    def change_comment(self, comment):
        log('====chenge comment START====')
        return check_db.change_comment(self.db, str(comment))

    def check_firmware_key(self, key_id, rom = None):
        log('====check_firmware_key START====')
        return check_db.check_fw_key(self.db, int(key_id), rom)

    def check_script_ready(self, id):
        log('====check script ready START====')
        return check_db.check_script_ready(self.db, id)

    def get_last_signfile_id(self):
        log('==== get last signfile id START ====')
        return check_db.get_last_signfile_id(self.db)

    def check_script_refuse(self, id):
        log('====check script refuse START====')
        return check_db.check_script_refuse(self.db, id)

    def delete_file(self):
        log('====delete file====')
        return check_db.click_delete()

    def delete_sign_file(self):
        log("====delete sign file START====")
        return check_db.delete_sign_file(self.db, None)

    def delete_last_sign_file(self):
        log("====delete last sign file START====")
        return check_db.delete_sign_file(self.db, 'last_file')

    def prep_for_test_with_fw_keys(self):
        log("====prep to fw keys START====")
        return check_db.prep_to_test_with_fw_keys()

    def add_no_active_user_trying_him_to_login(self):
        log("====add no active user START====")
        return check_db.add_no_active_user_trying_him_to_login()

    def load_config_file_to_db(self, count, filename):
        log("====load config file to db START=====")
        rows_before_add = check_db.get_number_fwkeys_firmware_keys(self.db)
        path = ssrv.generate_config_file(int(count), filename)
        log("==config was generated==")
        ssrv.load_key_to_db('ssrv_load_config.sh', path)
        log("===config was load to db===")
        rows_after_add = check_db.get_number_fwkeys_firmware_keys(self.db)
        assert (rows_after_add == (rows_before_add + int(count) - 6)), 'ERROR, config file was loaded not correct'

    def import_firmware_keys_version_one(self, count, filename, start_id):
        log("====import firmware keys Version 1.0 START=====")
        path = ssrv.generate_firmware_keys(int(count), filename, 1, int(start_id), 'Version 1.0')
        log("File was generated")
        ssrv.load_key_to_db('ssrv_load_keys.sh', path)
        log('File was loaded')
        # path = '/home/stp/in/fileimport1'
        return check_db.check_imported_fwkeys_version_one(self.db, path, int(count), int(start_id))

    def import_firmware_keys_version_two(self, count, filename, start_id):
        log("====import firmware keys Version 1.0 START=====")
        path = ssrv.generate_firmware_keys(int(count), filename, 2, int(start_id), 'Version 2.0')
        # path = '/home/stp/in/ImportFirmwareKeysVersion2.0_1575970682'
        ssrv.load_key_to_db('ssrv_load_keys.sh', path)
        return check_db.check_imported_fwkeys_version_two(self.db, path, int(count), int(start_id))

    def import_firmware_keys_different_version_and_data(self, count, filename, start_id, version, version_name=''):
        log("====Import firmware keys %s=====" % version_name)
        path = ssrv.generate_firmware_keys(int(count), filename, version, int(start_id), version_name)
        count_before_add = check_db.get_count_of_key_value(self.db)
        ssrv.load_key_to_db('ssrv_load_keys.sh', path)
        count_after_add = check_db.get_count_of_key_value(self.db)
        assert (count_after_add == count_before_add), 'ERROR, keys was added in db'
        return 1

    def change_script_file(self):
        log('====Change script file START====')

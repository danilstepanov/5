
class ConfigHelper(object):

    is_init = False

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ConfigHelper, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if ConfigHelper.is_init:
            return
        dict = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in open('/home/stp/ssrv_tests/keywords/ssrv_config.txt')}
        #dict = {line.split('=')[0].strip(): line.split('=')[1].strip() for line in open('/home/jenkins/workspace/ss_deploy/keywords/ssrv_config.txt')}
        self.path_to_bbmk=dict.get('path_to_bbmk')
        self.database_ip=dict.get('database_ip')
        self.db_port=dict.get('db_port')
        self.db_name=dict.get('db_name')
        self.db_user=dict.get('db_user')
        self.host_ip=dict.get('host_ip')

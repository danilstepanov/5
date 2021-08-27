import psycopg2
import random
from system_command import *
import os,binascii



keyid = lambda i: "%0.8x" % i

def check_db_user(user):
    conn = psycopg2.connect(dbname='signserver', user='signserveradmin')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM ssrv.auth_user")
    row = cursor.fetchall()
    cursor.close()
    conn.close()
    for i in row:
        if user == i[0]:
            return 1
    return 0


def check_db_permission(name, status):
    conn = psycopg2.connect(dbname='signserver', user='signserveradmin')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, can_approve FROM ssrv.signserver_permission")
    row = cursor.fetchall()
    cursor.execute("SELECT id, username FROM ssrv.auth_user")
    row1 = cursor.fetchall()
    cursor.close()
    conn.close()
    if status == 'False':
        status = False
    else:
        status = True
    for i in row1:
        if name == i[1]:
            id = i[0]
    for i in row:
        if id == i[0] and status == i[1]:
            return 1
    return 0


def generate_firmware_keys(count, filename, version, start_id, version_name):
    count = count + start_id
    path = get_homedir_in() + '/' + filename
    with open(path, 'w') as f:
        if version == 1:
            f.write('%s\n' % version_name)
            for i in xrange(start_id, count):
                f.write('%s;%s\n' % (keyid(i), binascii.b2a_hex(os.urandom(random.randint(16, 80)))))
        elif version == 2:
            f.write('%s\n' % version_name)
            for i in xrange(start_id, count):
                rom = random.choice(('1', '0', ''))
                f.write('%s;%s;%s;%s;\n' % (keyid(i), binascii.b2a_hex(os.urandom(random.randint(16, 80))), rom, rom))
    return path

def generate_config_file(count, filename):
    count += 1
    path = get_homedir_in() + '/' + filename
    typekeys = ['Aes_key_256_linked', 'Aes_iv_128_linked', 'Rsa_pub_exp_2048_linked', 'aes128_not_linked', 'Rsa2048_not_linked']
    with open(path, 'w') as f:
        f.write('Version 1.0\n\n')
        f.write('Configuration\n')
        for i in range(7, count):
            f.write('00000005;DeviceClassWithFW;00000082;ParttypeWithFW;;;%s;%s\n' % (keyid(i), random.choice(typekeys)+str(i)))
    return path

def load_key_to_db(scriptname, path_to_keys_file):
    path = lambda name: os.popen('sudo locate "%s"'% (name)).read()[:-1]
    os.popen('rm -Rf ~/.local/share/Trash')
    os.popen('sudo updatedb')
    path_to_script = path(scriptname)
    command = 'echo "1" | sudo -S -u postgres %s %s' % (path_to_script, path_to_keys_file)
    os.popen(command).read()
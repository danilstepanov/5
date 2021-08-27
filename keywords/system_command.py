import os

def get_homedir_out():
    cur_dir = os.getcwd()
    home_dir = '/' + '/'.join(cur_dir.split('/')[1:3])
    return os.path.join(home_dir, 'out')

def get_homedir_in():
    cur_dir = os.getcwd()
    home_dir = '/' + '/'.join(cur_dir.split('/')[1:3])
    return os.path.join(home_dir, 'in')

def docker_cp_from_ssrv_web(path_to_file):
    path_from_container = '%s%s' % ("/var/www/SignServer/media/", path_to_file)
    command = "%s%s%s%s" % ('docker cp ssrv_web:', path_from_container, ' ', get_homedir_out())
    assert (os.system(command) == 0), "ERROR cp from ssrv web"
    return 1


def docker_cp_to_ssrv_lib_hasp(filename):
    path_to_file = "%s%s" % (get_homedir_in(), '/')
    command = "%s%s%s%s" % ('docker cp ', path_to_file, filename, "docker_ssrv_lib_debian_8_1:/opt/kmi/bin/")
    assert (os.system(command) == 0), "ERROR cp to ssrv_lib_hasp, DEBIAN"
    command1 = "%s%s%s%s" % ('docker cp ', path_to_file, filename, "docker_ssrv_lib_ubuntu_18_1:/opt/kmi/bin/")
    assert (os.system(command1) == 0), "ERROR cp to ssrv_lib_hasp, UBUNTU"
    return 1

def docker_cp_from_ssrv_lib_hasp(path_to_file):
    command = "%s%s%s%s" % ('docker cp ssrv_lib:', path_to_file, ' ', get_homedir_out())
    assert (os.system(command) == 0), "ERROR cp from ssrv_lib_hasp"
    return 1

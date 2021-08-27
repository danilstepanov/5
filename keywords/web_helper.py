import random
from selenium.webdriver import Chrome
import time
from Logger import get_logger, log


driver = Chrome(executable_path="/usr/local/lib/python2.7/dist-packages/chromedriver_binary/chromedriver")

def login_to_site(username, passwd):
    driver.get("https://192.168.14.42:443")
    driver.find_element_by_id("id_username").send_keys('stp')
    driver.find_element_by_id("id_password").send_keys('1')
    driver.find_element_by_class_name("main").click()


import time
import getpass
import os
from selenium import webdriver

max_wait_time = 30

def login(driver):

    if not os.path.exists("config/login"):
        login = raw_input("login: ")
    else:
        file_ = open("config/login")
        login = file_.readlines()
    #
    if not os.path.exists("config/passwd"):
        passwd = getpass.getpass()
    else:
        file_ = open("config/passwd")
        passwd = file_.readlines()


    driver.get("http://www.managerzone.com/")

    print driver.current_url

    driver.find_element_by_id('login_username').send_keys(login)
    driver.find_element_by_id('login_password').send_keys(passwd)

    driver.find_element_by_id('login').click()


    t = time.time()
    logged_in = False
    while not logged_in:
        if time.time() - t > max_wait_time:
            break

        try:
            test = driver.find_element_by_id("logout_etc")
            print "login succesfull"
            logged_in = True
        except:
            time.sleep(1)
    
    if not logged_in:
        print "failed to login"
        driver.save_screenshot("errors/"+str(t)+"_login_failed.png")
        exit()

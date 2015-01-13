import time
import getpass
import os
import sys
from selenium import webdriver

max_wait_time = 30
login = None
passwd = None
fails_in_a_row = 0
max_fails_before_exit = 10

def get_login_data():
    global passwd, login

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

def load_main_page_and_log_in(driver):
    global fails_in_a_row, max_fails_before_exit

    print "loading main page"
    driver.get("http://www.managerzone.com/")
    print "page loaded", driver.current_url
    print "waiting for content"

    try:
        driver.find_element_by_tag_name('head')#wait for load
        send_login_data(driver)
        fails_in_a_row = 0
    except Exception:
        print "failed"
        fails_in_a_row = fails_in_a_row + 1
        if fails_in_a_row < max_fails_before_exit:
            load_main_page(driver)
        else:
            print "unable to load main page... program is terminating..."
            return False
    return True

def send_login_data(driver):
    global passwd, login

    print "trying to fill and send login form"

    try:
        driver.find_element_by_id('login_username').send_keys(login)
        driver.find_element_by_id('login_password').send_keys(passwd)

        driver.find_element_by_id('login').click()
        
        print "form sent"
    except Exception:
        print "failed to fill and send login form!"
        raise Exception("Failed to fill and send login form!")

def wait_for_login_response(driver):
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
        return False
    return True

def login(driver):
    global passwd, login

    get_login_data()
    if not load_main_page_and_log_in(driver):
        return False
    if not wait_for_login_response(driver):
        return False

    return True



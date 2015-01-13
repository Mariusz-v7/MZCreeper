#-*- coding: utf-8 -*-
import time
import getpass
import os
from selenium import webdriver

from selenium.webdriver.support.ui import Select

max_wait_time = 60
#page_url = "http://gamesstats.hopto.org/"
#page_url = "http://gamesstats.loc/"



def login(driver):
    file_ = open("config/upload")
    page_url = file_.readlines()
    page_url = page_url[-1]#\n
    page_url = page_url[0:-1]#\n

    print "trying to login on " + page_url


    if not os.path.exists("config/logings"):
        login = raw_input("login: ")
    else:
        file_ = open("config/logings")
        login = file_.read()
        login = login[0:-1] #remove \n... wtf..?
    #
    if not os.path.exists("config/passwdgs"):
        passwd = getpass.getpass()
    else:
        file_ = open("config/passwdgs")
        passwd = file_.read()
        passwd = passwd[0:-1] #remove \n... wtf..?



    print "loading page " + page_url
    driver.get(page_url)
    print "page loaded", driver.current_url
    print "waiting for content"
    try:
        driver.find_element_by_tag_name('head')
    except Exception:
        print "failed"
        return False

    print "trying to fill and send login form"

    try:
        driver.find_element_by_id('login').send_keys(login)
        driver.find_element_by_id('pass').send_keys(passwd)

        driver.find_element_by_tag_name('button').click()
    except Exception:
        print "failed"
        return False


    t = time.time()
    logged_in = False
    while not logged_in:
        if time.time() - t > max_wait_time:
            break

        try:
            test = driver.find_element_by_class_name("error0")
            print "login succesfull"
            logged_in = True
        except:
            time.sleep(1)
    
    if not logged_in:
        print "failed to login"
        try:
            driver.save_screenshot("errors/"+str(t)+"_logings_failed.png")
        except Exception:
            print "failed to save screenshot"
        return False
    return True


def training(driver):
    file_ = open("config/upload")
    page_url = file_.readlines()
    page_url = page_url[-1]
    page_url = page_url[0:-1]+"/upload" #\n


    trainings = os.listdir("upload/training_reports")
    for training in trainings:
        print "trying to load page " + page_url
        driver.get(page_url)
        print "page loaded, waiting for content"

        try:
            driver.find_element_by_tag_name('head')
        except Exception:
            print "failed"
            return False

        print "tying to send report"

        try: 
            file_ = open("upload/training_reports/"+training)
            data = file_.read()
            driver.find_element_by_tag_name('textarea').send_keys(data)
            driver.find_element_by_tag_name('button').click()
            time.sleep(5)
            driver.find_element_by_tag_name('head')

            os.remove("upload/training_reports/"+training)
        except Exception:
            print "failed"
            return False
    return True

def squad(driver):
    file_ = open("config/upload")
    page_url = file_.readlines()
    page_url = page_url[-1]
    page_url = page_url[0:-1]+"/upload" #\n


    trainings = os.listdir("upload/squad")
    for training in trainings:
        print "trying to load page " + page_url
        driver.get(page_url)
        print "page loaded, waiting for content"
        try:
            driver.find_element_by_tag_name('head')
        except Exception:
            print "failed"
            return False

        print "trying to send squad"
        try:
            select = Select(driver.find_element_by_tag_name("select"))
            select.select_by_value("mz_soccer_squad")

            file_ = open("upload/squad/"+training)
            data = file_.read()
            data = unicode(data, errors='replace')
            driver.find_element_by_tag_name('textarea').send_keys(data)
            driver.find_element_by_tag_name('button').click()
            time.sleep(5)
            driver.find_element_by_tag_name('head')

            os.remove("upload/squad/"+training)
        except Exception:
            print "failed"
            return False
    return True


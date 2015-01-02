#-*- coding: utf-8 -*-
import time
import getpass
import os
from selenium import webdriver

from selenium.webdriver.support.ui import Select

max_wait_time = 60
page_url = "http://gamesstats.hopto.org/"
#page_url = "http://gamesstats.loc/"

def login(driver):
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



    #driver.get("http://www.mrugames.hopto.org/")
    driver.get(page_url)
    driver.find_element_by_tag_name('head')


    driver.find_element_by_id('login').send_keys(login)
    driver.find_element_by_id('pass').send_keys(passwd)

    driver.find_element_by_tag_name('button').click()


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
        driver.save_screenshot("errors/"+str(t)+"_logings_failed.png")
        exit()

def training(driver):

    trainings = os.listdir("upload/training_reports")
    for training in trainings:
        driver.get(page_url+"/upload")
        driver.find_element_by_tag_name('head')


        file_ = open("upload/training_reports/"+training)
        data = file_.read()
        driver.find_element_by_tag_name('textarea').send_keys(data)
        driver.find_element_by_tag_name('button').click()
        time.sleep(5)
        driver.find_element_by_tag_name('head')

        os.remove("upload/training_reports/"+training)

def squad(driver):

    trainings = os.listdir("upload/squad")
    for training in trainings:
        driver.get(page_url+"/upload")
        driver.find_element_by_tag_name('head')

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


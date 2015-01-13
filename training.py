# -*- coding: utf-8 -*-

from selenium import webdriver
import login
import time
import datetime
import os
import sys
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui


days_names = ["weekly", "monday", "tuesday", "wednesday", "thurstay", "friday", "saturday"]
max_fails_before_exit = 1
fails_in_a_row = 0

def load_training_page(driver):
    global fails_in_a_row

    print "loading training page"
    driver.get("http://www.managerzone.com/?p=training_report")
    print "page loaded", driver.current_url
    print "waiting for content"
    try:
        driver.find_element_by_tag_name('head')#wait for load
        fails_in_a_row = 0
    except Exception:
        print "failed"
        fails_in_a_row = fails_in_a_row + 1
        if fails_in_a_row < max_fails_before_exit:
            load_training_page(driver)
        else:
            print "unable to load training page... program is terminating..."
            sys.exit()
def select_day(driver, day):
    print "trying to select " + days_names[day] + " training"
    time.sleep(30)
    try:
        link = driver.find_element_by_id("training_report_header_"+str(day)).find_elements_by_tag_name("a")[0].click()
    except Exception:
        print "failed"
        pass

    time.sleep(30)
def get_training(driver, training_date):
    print "trying to get training data"
    try:
        training_parent = driver.find_element_by_id("training_report")
        training_table = training_parent.find_elements_by_class_name('report_table');

        print "training data got, saving to file training_reports/"+training_date+".html"

        file_ = open("training_reports/"+training_date+".html", 'w')
        file_.write(training_parent.get_attribute("innerHTML").encode('UTF-8'))
        file_.close()
    except Exception:
        print "failed to find training report..."
        t = time.time()
        try:
            driver.save_screenshot("errors/"+str(t)+"_login_failed.png")
        except Exception:
            print "failed to save screenshot"



def training(driver):
    weekday = datetime.datetime.today().weekday()
    #0 - poniedzialek
    #1 - wtorek
    #etc
    ###
    load_training_page(driver)

    today_date = time.strftime("%Y-%m-%d")
    today_daynumber = int(time.strftime("%w"))
    week_number = time.strftime("%W")

    monday_date = datetime.datetime.strptime(today_date, "%Y-%m-%d")
    monday_date = monday_date + datetime.timedelta(days = -today_daynumber)

    for i in range(1, today_daynumber + 1):
        training_date_ = monday_date + datetime.timedelta(days = +(i))
        training_date = training_date_.strftime("%Y-%m-%d")

        if os.path.exists("training_reports/"+training_date+".html"):
            print 'skip ', days_names[i]
            continue

        select_day(driver, i)
        get_training(driver, training_date)










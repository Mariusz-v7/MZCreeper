# -*- coding: utf-8 -*-

from selenium import webdriver
import login
import time
import datetime
import os
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui


def training(driver):
    weekday = datetime.datetime.today().weekday()
    #0 - poniedzialek
    #1 - wtorek
    #etc
    ###
    driver.get("http://www.managerzone.com/?p=training_report")
    driver.find_element_by_tag_name('head')#wait for load

    print driver.current_url

    today_date = time.strftime("%Y-%m-%d")
    today_daynumber = int(time.strftime("%w"))
    week_number = time.strftime("%W")

    monday_date = datetime.datetime.strptime(today_date, "%Y-%m-%d")
    monday_date = monday_date + datetime.timedelta(days = -today_daynumber)

    days_names = ["weekly", "monday", "tuesday", "wednesday", "thurstay", "friday", "saturday"]
    for i in range(1, today_daynumber + 1):
        training_date_ = monday_date + datetime.timedelta(days = +(i - 1))
        training_date = training_date_.strftime("%Y-%m-%d")

        if os.path.exists("training_reports/"+training_date+".html"):
            print 'skip ', days_names[i]
            continue


        print i, days_names[i] + " training"

        time.sleep(5)
        link = driver.find_element_by_id("training_report_header_"+str(i)).find_elements_by_tag_name("a")[0].click()
        time.sleep(5)
        wait = ui.WebDriverWait(driver, 30)
        wait.until(lambda driver: driver.find_element_by_id("training_report"))





        training_parent = driver.find_element_by_id("training_report")
        training_table = training_parent.find_elements_by_class_name('report_table');

        file_ = open("training_reports/"+training_date+".html", 'w')
        file_.write(training_parent.get_attribute("innerHTML").encode('UTF-8'))
        file_.close()



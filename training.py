# -*- coding: utf-8 -*-

from selenium import webdriver
import login
import time
import datetime
import os


def training(driver):
    weekday = datetime.datetime.today().weekday()
    #0 - poniedzialek
    #1 - wtorek
    #etc
    ###
    driver.get("http://www.managerzone.com/?p=training_report")

    print driver.current_url

    date = time.strftime("%Y-%m-%d")

    if not os.path.exists("training_reports/"+date):
        os.makedirs("training_reports/"+date)

    days_names = ["weekly", "monday", "tuesday", "wednesday", "thurstay", "friday", "saturday"]
    for i in range(0, 7):
        print days_names[i] + " training"

        link = driver.find_element_by_id("training_report_header_"+str(i)).find_elements_by_tag_name("a")[0].click()
        time.sleep(5)


        training_parent = driver.find_element_by_id("training_report")
        training_table = training_parent.find_elements_by_class_name('report_table');

        file_ = open("training_reports/"+date+"/report_"+days_names[i]+".html", 'w')
        file_.write(training_parent.get_attribute("innerHTML").encode('UTF-8'))
        file_.close()


###
#   tabi = 0
#   for tab in training_table:
#       divs = tab.find_elements_by_tag_name('div')
#       if tabi > 0:
#           name = divs[3].text
#           skill = divs[5].text
#           progress = divs[9].find_element_by_tag_name('img').get_attribute('src')
#           progress = progress.split('/')
#           progress = progress[-1]
#        
#           test = db.Execute("SELECT `id` FROM `training` WHERE `player`="+db.prepare(name)+" AND `date`=CURRENT_DATE()")
#           if test.EOF:
#               db.Execute("""INSERT INTO `training`(`player`,`skill`,`progress`,`date`) 
#                   VALUES("""+db.prepare(name)+""","""+db.prepare(skill)+""","""+db.prepare(progress)+""",CURRENT_DATE())""")
#       tabi += 1
    





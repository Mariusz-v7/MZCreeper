from selenium import webdriver
import login
import time
import datetime
import os


def squad(driver):
    driver.get("http://www.managerzone.com/?p=players&sub=alt")
    driver.find_element_by_tag_name('head')#wait for load

    print driver.current_url

    date = time.strftime("%Y-%m-%d")
    if not os.path.exists("squad/"+date):
        os.makedirs("squad/"+date)

    table = driver.find_element_by_id("squad_summary")

    file_ = open("squad/"+date+"/squad.html", 'w')
    file_.write(table.get_attribute("innerHTML").encode('UTF-8'))
    file_.close()

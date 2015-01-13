from selenium import webdriver
import login
import time
import datetime
import os


def squad(driver):
    print "trying to load squad page"
    driver.get("http://www.managerzone.com/?p=players&sub=alt")
    print "page loaded", driver.current_url
    print "waiting for content"
    try:
        driver.find_element_by_tag_name('head')#wait for load
    except Exception:
        print "failed to load content"
        return False


    date = time.strftime("%Y-%m-%d")

    print "getting squad data"
    try:
        table = driver.find_element_by_id("squad_summary")
    except Exception:
        print "failed to get training data"
        return False

    print "squad data got, saving to file squad/"+date+".html"
    file_ = open("squad/"+date+".html", 'w')
    file_.write(table.get_attribute("innerHTML").encode('UTF-8'))
    file_.close()

    print "done"
    return True

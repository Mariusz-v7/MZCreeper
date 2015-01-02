#!/usr/bin/python

import os
import getpass
from selenium import webdriver
import login
import training
import squad

########################################################################################
driver = webdriver.PhantomJS("lib/phantomjs")
########################################################################################

if not os.path.exists("lib"):
    os.makedirs("lib")
if not os.path.exists("config"):
    os.makedirs("config")
if not os.path.exists("squad"):
    os.makedirs("squad")
if not os.path.exists("training_reports"):
    os.makedirs("training_reports")
if not os.path.exists("errors"):
    os.makedirs("errors")
if not os.path.exists("upload"):
    os.makedirs("upload")
if not os.path.exists("upload/training_reports"):
    os.makedirs("upload/training_reports")
if not os.path.exists("upload/squad"):
    os.makedirs("upload/squad")

login.login(driver)
training.training(driver)
squad.squad(driver)



driver.quit()


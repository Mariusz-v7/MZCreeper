#!/usr/bin/python

import os
import getpass
from selenium import webdriver
import login
import training
import squad
import parse_squads

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

#login.login(driver)
#training.training(driver)
#squad.squad(driver)

parse_squads.parse()


driver.quit()


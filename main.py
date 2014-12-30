#!/usr/bin/python

import getpass
from selenium import webdriver
import login
import training
import squad


driver = webdriver.PhantomJS("lib/phantomjs")


login.login(driver)
training.training(driver)
squad.squad(driver)



driver.quit()


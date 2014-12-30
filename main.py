#!/usr/bin/python

import getpass
from selenium import webdriver
import login
import training


driver = webdriver.PhantomJS("lib/phantomjs")


login.login(driver)
training.training(driver)



driver.quit()


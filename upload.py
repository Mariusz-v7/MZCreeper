#!/usr/bin/python
#-*- coding: utf-8 -*-

import upload_all

import os
import getpass
from selenium import webdriver
import login
import training
import squad

driver = webdriver.PhantomJS("lib/phantomjs")

if upload_all.login(driver):
    upload_all.training(driver)
    upload_all.squad(driver)

driver.close()
driver.quit()

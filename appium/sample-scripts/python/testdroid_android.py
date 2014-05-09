##
## For help on setting up your machine and configuring this TestScript go to
## http://help.testdroid.com/customer/portal/topics/631129-appium/articles
##

import os
import sys
import time
from time import sleep
from selenium import webdriver

def log(msg):
    print (time.strftime("%H:%M:%S") + ": " + msg)

appium_Url = 'http://appium.testdroid.com/wd/hub';

##
## IMPORTANT: Set the following parameters.
##
screenshotDir= "/absolute/path/to/desired/directory"
testdroid_username = "user@example.com"
testdroid_password = "p4s$w0rd"

testdroid_device = "LG Google Nexus 5 D821 4.4" # Example device. Change if you desire.

desired_capabilities_cloud = {}
desired_capabilities_cloud['testdroid_username'] = testdroid_username
desired_capabilities_cloud['testdroid_password'] = testdroid_password
desired_capabilities_cloud['testdroid_project'] = 'Appium Android Demo'
desired_capabilities_cloud['testdroid_testrun'] = 'TestRun A'
desired_capabilities_cloud['testdroid_device'] = testdroid_device
desired_capabilities_cloud['testdroid_app'] = 'sample/BitbarAndroidSample.apk'
desired_capabilities_cloud['device'] = 'Android'
desired_capabilities_cloud['app-package'] = 'com.bitbar.testdroid'
desired_capabilities_cloud['app-activity'] = '.BitbarSampleApplicationActivity'

desired_caps = desired_capabilities_cloud;

log ("Will save screenshots at: " + screenshotDir)

# set up webdriver
log ("WebDriver request initiated. Waiting for response, this typically takes 2-3 mins")
driver = webdriver.Remote(appium_Url, desired_caps)
log ("WebDriver response received")

log ("Activity-1")
log ("  Getting device screen size")
print driver.get_window_size()

sleep(2) # always sleep before taking screenshot to let transition animations finish
log ("  Taking screenshot: 1_appLaunch.png")
driver.save_screenshot(screenshotDir + "/1_appLaunch.png")

log ("  Typing in name")
elems=driver.find_elements_by_tag_name('EditText')
log ("  info: EditText:" + `len(elems)`)
log ("  Filling in name")
elems[0].click()
elems[0].send_keys("Testdroid User")
sleep(2)
log ("  Taking screenshot: 2_nameTyped.png")
driver.save_screenshot(screenshotDir + "/2_nameTyped.png")
log ("  Hiding keyboard")
driver.back()
sleep(2)
log ("  Taking screenshot: 3_nameTypedKeyboardHidden.png")
driver.save_screenshot(screenshotDir + "/3_nameTypedKeyboardHidden.png")

log ("  Clicking element 'Buy 101 devices'")
elem = driver.find_element_by_name('Buy 101 devices')
elem.click()
sleep(2)
log ("  Taking screenshot: 4_clickedButton1.png")
driver.save_screenshot(screenshotDir + "/4_clickedButton1.png")

log ("  Clicking Answer")
elem = driver.find_element_by_name('Answer')
elem.click()
sleep(2)
log ("  Taking screenshot: 5_answer.png")
driver.save_screenshot(screenshotDir + "/5_answer.png")

log ("Navigating back to Activity-1")
driver.back()
sleep(2)
log ("  Taking screenshot: 6_mainActivity.png")
driver.save_screenshot(screenshotDir + "/6_mainActivity.png")

log ("  Clicking element 'Use Testdroid Cloud'")
elem = driver.find_element_by_name('Use Testdroid Cloud')
elem.click()
sleep(2)
log ("  Taking screenshot: 7_clickedButton2.png")
driver.save_screenshot(screenshotDir + "/7_clickedButton2.png")

log ("  Clicking Answer")
elem = driver.find_element_by_name('Answer')
elem.click()
sleep(2)
log ("  Taking screenshot: 8_answer.png")
driver.save_screenshot(screenshotDir + "/8_answer.png")

log ("Quitting")
driver.quit()
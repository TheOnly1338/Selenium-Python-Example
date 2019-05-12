from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
#chrome_options.add_argument("headless")
usr = raw_input("Email: ")
pwd = raw_input("Password: ")

driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get('https://facebook.com')

print ("Website Opened")
sleep(1)
username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Details Entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password Has Been Entered")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print("Task Completed")

print ("Program Completed!")

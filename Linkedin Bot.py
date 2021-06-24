#libraries to import
import os, time, random, getpass, smtplib, sys, fileinput
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from time import sleep

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)



# driver commands linkedin 

driver.set_window_size(1024, 768)
driver.maximize_window()
driver.get('https://www.linkedin.com/login')
time.sleep(0.5)

# driver inputs credentials
email = driver.find_element_by_xpath('//*[@id="search"]')
email.send_keys('rskaliraman1@gmail.com')
time.sleep(0.6)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Sneh123#')
time.sleep(0.5)

# driver finds and commannds sign in button on linkedin 
login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()
time.sleep(0.4)

# create search query on linkedin
driver.get('https://www.linkedin.com/jobs/search/')
search = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember58"]')
search.send_keys('Data Analyst')    
searchlocation = driver.find_element_by_xpath('//*[@id="jobs-search-box-location-id-ember58"]')
searchlocation.send_keys(' 10001')
searchbutton = driver.find_element_by_xpath('//*[@id="ember58"]/button')
searchbutton.click()
time.sleep(0.7)


import pyautogui
pyautogui.FAILSAFE = True
pyautogui.moveTo(1213, 282, duration=0.5)
pyautogui.click(x=1213, y=282, clicks=1, interval=1, button='left')
time.sleep(0.5)
pyautogui.FAILSAFE = True
pyautogui.moveTo(1038, 461, duration=0.6)
pyautogui.click(x=1038, y=461, clicks=1, interval=1, button='left')
pyautogui.FAILSAFE = True
pyautogui.moveTo(1458, 527, duration=0.5)
pyautogui.click(x=1458, y=527, clicks=1, interval=1, button='left')
time.sleep(0.5)
pyautogui.FAILSAFE = True
pyautogui.moveTo(1470, 600, duration=0.5)
pyautogui.click(x=1470, y=600, clicks=2, interval=1, button='left')
pyautogui.FAILSAFE = True
pyautogui.moveTo(1335, 979, duration=0.5)
pyautogui.click(x=1335, y=979, clicks=2, interval=1, button='left')
time.sleep(0.5)
pyautogui.FAILSAFE = True
pyautogui.moveTo(1467, 653, duration=0.5)
pyautogui.click(x=14675, y=653, clicks=2, interval=1, button='left')



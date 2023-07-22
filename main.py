import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd
from threading import Thread, BoundedSemaphore
from peewee import *

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40)

driver.get('https://arrs.host/')
driver.switch_to.window(driver.window_handles[-1])
time.sleep(15)
textarea = driver.find_element(By.XPATH, '//*[@id=\'cmd_input\']')

f = open('1.txt')
l = [str(i) for i in f]

for item in l:
    textarea.send_keys("login observer54-5")
    time.sleep(1)
    textarea.send_keys(Keys.ENTER)
    time.sleep(8)
    textarea.send_keys(item)
    time.sleep(8)

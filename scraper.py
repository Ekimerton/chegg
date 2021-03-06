import os
import time
import urllib.request
import random

# Selenium Imports DON'T TOUCH!!
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def get_page(url):
    global logged_in

    # Login creds
    global email
    global password


    if not logged_in:
        # Login
        browser.get("https://www.chegg.com/my/account")
        element = wait.until(EC.presence_of_element_located((By.ID, 'emailForSignIn')))
        element.send_keys(email)
        element = wait.until(EC.presence_of_element_located((By.ID, 'passwordForSignIn')))
        element.send_keys(password)
        element = browser.find_element_by_name('login')
        element.click()

        # Wait until login complete
        element = wait.until(EC.presence_of_element_located((By.ID, 'orders-card')))
        logged_in = True

    # Handle request
    browser.get(url)
    element = browser.find_element_by_class_name('answer-given-body')
    print(element.text)

logged_in = False
browser = webdriver.Chrome()
browser.set_window_size(600, 324)
wait = WebDriverWait(browser, 30)

email = os.environ['chegg_username']
password = os.environ['chegg_password']


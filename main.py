from selenium import webdriver
from time import sleep
import requests
import base64

use_r = base64.b64decode('username').decode("utf-8")
# encoded username
# base64.b64encode("username").decode("utf-8")
pass_word = base64.b64decode('password').decode("utf-8")
# encoded password
# base64.b64encode("password").decode("utf-8")

driver = webdriver.Chrome("D:/BrowserDrivers/chromedriver") # Chrome webdrivers path
url = 'https://www.facebook.com/'
timeout = 5
try:
    request = requests.get(url, timeout=timeout)
    print("Connected to the Internet.")
    driver.get(url)
    print("Opened facebook")
    sleep(2)
    username_box = driver.find_element_by_id('email')
    username_box.send_keys(use_r)
    print("Email Id entered")
    sleep(2)
    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pass_word)
    print("Password entered")
    login_box = driver.find_element_by_name('login')
    login_box.click()
    print('Done')
except (requests.ConnectionError, requests.Timeout)  as exception:
    print("No internet connection.")

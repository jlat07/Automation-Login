import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


load_dotenv()
# load, get, and set env variables from .env file
ZIP_CODE_PW = os.environ.get("ZIP_CODE_PW")
ZIP_CODE_USERNAME = os.environ.get("ZIP_CODE_USERNAME")

# url you wish to access
URL = "https://school.zipcode.rocks/"

# create a new Chrome session
browser = webdriver.Chrome()
browser.implicitly_wait(1)

# navigate to zip code portal login page
browser.get(URL)

# get the username textbox
username_field = browser.find_element_by_name("name")
username_field.clear()

# enter username
username_field.send_keys(ZIP_CODE_USERNAME)
time.sleep(1)

# get the password textbox
password_field = browser.find_element_by_name("pass")
password_field.clear()

# enter password and return to login
password_field.send_keys(ZIP_CODE_PW)
password_field.send_keys(Keys.RETURN)
time.sleep(1)

# get anttendance button and submit attendance
try:
    attendance = browser.find_element_by_id("edit-submit-button")
    attendance.click()
    print("You signed in")
except:
    print('You are already signed in')

time.sleep(1)

browser.close()
quit()

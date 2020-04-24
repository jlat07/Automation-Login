import os
import time
import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


load_dotenv()
# load, get, and set env variables from .env file
ZIP_CODE_PW = os.environ.get("ZIP_CODE_PW")
ZIP_CODE_USERNAME = os.environ.get("ZIP_CODE_USERNAME")

# url you wish to access
URL = "https://school.zipcode.rocks/"

# set date for screenshot file
dt = datetime.datetime.now()
date = dt.strftime("%Y-%m-%d %H.%M.%S")

# create a new Chrome session/with options to run headless
options = Options()
options.headless = True
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(3)

# navigate to zip code portal login page
browser.get(URL)

# expand full browser
browser.maximize_window()

# get the username textbox
username_field = browser.find_element_by_name("name")
username_field.clear()

# enter username
username_field.send_keys(ZIP_CODE_USERNAME)
#time.sleep(1)

# get the password textbox
password_field = browser.find_element_by_name("pass")
password_field.clear()

# enter password and return to login
password_field.send_keys(ZIP_CODE_PW)
password_field.send_keys(Keys.RETURN)
#time.sleep(1)

# select attendance button, submit attendance, take a screenshot for documentation proof 
try:
    attendance = browser.find_element_by_id("edit-submit-button")
    attendance.click()
    print("You signed in")
    browser.save_screenshot(f"attendance_{date}.png")
except:
    print('You are already signed in')
    #browser.save_screenshot(f"already_signed_in_{date}.png")

time.sleep(1)

browser.close()

quit()
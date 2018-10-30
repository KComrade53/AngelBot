import time
from selenium import webdriver
from secrets import *

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("https://app.reef-education.com/#/courses")
driver.find_element_by_id("userEmail").send_keys(userName)
driver.find_element_by_id("userPassword").send_keys(password)
driver.find_element_by_id("sign-in-button").click()
# time.sleep(10)
# driver.quit()

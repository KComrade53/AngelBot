import time
from selenium import webdriver
from secrets import *

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("https://app.reef-education.com/#/courses")

# Log in
driver.find_element_by_id("userEmail").send_keys(userName)
driver.find_element_by_id("userPassword").send_keys(password)
driver.find_element_by_id("sign-in-button").click()
time.sleep(2)   # delays it so next findElement doesn't run too early

# Choose Angel course
driver.find_element_by_partial_link_text('Denis').click()
# time.sleep(10)
# driver.quit()

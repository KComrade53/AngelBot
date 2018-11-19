import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException
import winsound

from secrets import *

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
found = False
foundButton = False

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("https://app.reef-education.com/#/courses")
time.sleep(2)

# Log in
driver.find_element_by_id("userEmail").send_keys(userName)
driver.find_element_by_id("userPassword").send_keys(password)
driver.find_element_by_id("sign-in-button").click()
time.sleep(2)  # delays it so next findElement doesn't run too early

# Choose Angel course
driver.find_element_by_partial_link_text('Denis').click()
time.sleep(10)

while not found:
    try:
        driver.find_element_by_xpath('//button[text()="Join"]').click()  # only available when quiz is open
        found = True

        winsound.Beep(frequency, duration)
    except ElementNotVisibleException:
        print("Button not visible yet\n")
        time.sleep(20)
    except NoSuchElementException:
        print("Failed to find, trying again\n")
        time.sleep(20)
    except WebDriverException:  # catches rest of errors
        print("Chrome closed")
        driver.quit()
        break   # exit while loop

while 1:
    try:
        driver.find_element_by_id("multiple-choice-a").click()
        time.sleep(20)
        # foundButton = True
    except NoSuchElementException:
        print("Failed to find buttons, repeat\n")
        time.sleep(15)
    except ElementNotVisibleException:
        print("Button not visible yet\n")
        time.sleep(15)


# print(pew)
# driver.find_element_by_id('course-history-icon').click()  # for testing on course page

# Auto close - disable once done testing
# time.sleep(30)
# driver.quit()

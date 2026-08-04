# Using Checkbox Attribute 3.1 - 31-07-2026
# Page Start 86

# CHECKBOX #
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
checkbox2 = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")

# There is same method for: Check and Uncheck

# select the checkbox
checkbox1.click()
time.sleep(3)

# unselect the checkbox if selected
checkbox1.click()
time.sleep(3)

checkbox2.click()
time.sleep(3)

checkbox2.click()
time.sleep(3)

# To Know whether checkbox is selected or not

time.sleep(3)

if not checkbox1.is_selected(): # Click checkbox1 to select only if its NOT selected
    checkbox1.click()

time.sleep(3)

if checkbox1.is_selected():     # Click checkbox1 to Unselect only if its selected
    checkbox1.click()

time.sleep(10)

# Key Board Simulation 1.1 - 29-07-2026
# Get SeletorHub Extension
# Page Start 66

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# simulate keyboards keys
import time

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com")

# Get First Matching Element Only
# Relative XPath => "//input[@name='q']"
search_txtbox = driver.find_element(By.XPATH, "//input[@name='q']")

# For Error
# search_txtbox = driver.find_element(By.XPATH, "//input[@name='superman']")

print("Type of search_txtbox =>", type(search_txtbox))
time.sleep(3)

search_txtbox.send_keys('Iphone 17 Pro Max')
search_txtbox.send_keys(Keys.ENTER)

# quit driver
time.sleep(10)
driver.quit()

# Error: 
# NoSuchElementException: If element not found

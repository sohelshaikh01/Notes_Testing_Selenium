# Key Board Simulation 1.2 - 29-07-2026
# Differ in find_element & find_elements

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# simulate keyboards keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Get SeletorHub Extension
multi_search_txtbox = driver.find_elements(By.XPATH, "//textarea[@name='q']")

# Getting Type and Elements
print("Type of multi_search_txtbox =>", type(multi_search_txtbox))
print(multi_search_txtbox)

# It return list(array), you cannot perform activity

# It works only on single element
multi_search_txtbox.send_keys('Doomsday')
multi_search_txtbox.send_keys(Keys.ENTER)

time.sleep(60)

# Error:
# AttributeError: Wrong Attribute to Access

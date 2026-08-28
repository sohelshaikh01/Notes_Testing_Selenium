# Get Attribute 2.3 - 30-07-2026

# get_attribute()
# ● Fetches value of attribute for given web element
# ● It Returns value of attribute as:

# By default as string
# If attribute is boolean, then it returns as true or null
# If no attribute then it returns null

# GET ATTRIBUTE #
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
time.sleep(2)

print("maxlength: ", search_box.get_attribute("maxlength"))
print("id: ", search_box.get_attribute("id"))
print("value (before typing): ", search_box.get_attribute("value"))
time.sleep(2)

search_box.send_keys("IMCC")
print("value (after typing): ", search_box.get_attribute("value"))

time.sleep(2)
driver.quit()

# Selenium Navigation 1.3 - 29-07-2026
# Navigating Like Forward, Backward, etc.

# Driver.get() => Waits till whole page load

# COMMANDS:
# driver.get("www.google.com")
# forward()
# back()
# refresh()

# Perform: 
# Page reload -> forward -> refresh -> back

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# simulate keyboards keys
import time

driver = webdriver.Chrome()

# Open Medium
driver.get("https://medium.com")
print("Opened Medium.com")
time.sleep(3)

# Go to Dev.to
driver.get("https://dev.to")
print("Opened Dev.to")
time.sleep(3)

# Refresh Dev.to
driver.refresh()
print("Refreshed Dev.to")
time.sleep(3)

# Go back to Medium
driver.back()
print("Went back to Medium.com")
time.sleep(3)

# Go forward to Dev.to again
driver.forward()
print("Went forward to Dev.to")
time.sleep(3)

# Current Site Details - Navigation 2

print("Current URL =>", driver.current_url)
print("Current Page Title =>", driver.title)
# print("Current Page Source =>", driver.page_source)

# After Completion close driver instance to free up resources

print("Closing Driver")
driver.close()
driver.quit()

time.sleep(10)
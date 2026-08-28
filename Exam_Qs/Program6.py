# 2	Write a working executable code using any programming language like Python, Java, etc using
# Selenium to automate below test steps:
# 1. Open "https://www.tata.com/" in Chrome browser.
# 2. Click on "About" option present top left side of page
# 3. Now click on "Company Info" present in menu bar at top
# 4. Using Selenium navigation command, do navigate back to previous page
# 5. Using Selenium navigation command, do navigate forward
# 6. Using Selenium navigation command, refresh the current page

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.tata.com")

about = driver.find_element(By.XPATH, "//a[normalize-space()='About Us']")
about.click()
time.sleep(2)

company_info = driver.find_element(By.XPATH, "//a[normalize-space()='Companies']")
company_info.click()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(10)

driver.quit()
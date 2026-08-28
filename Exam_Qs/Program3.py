# B1	Write a working executable code using any programming language like Python, Java, etc using
# Selenium to automate below test steps:
# 1. Open "https://www.wikipedia.org/" in Chrome browser.
# 2. Make chrome browser window in full screen mode
# 3. Enter "Test Automation" in search textbox
# 4. Press keyboard "Enter" key
# 5. Fetch all cookies using Selenium and print those in IDE console.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

# full screen mode
driver.fullscreen_window()
time.sleep(2)

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Test Automation")
search_box.send_keys(Keys.ENTER)
time.sleep(2)

allCookies = driver.get_cookies()

for cookie in allCookies:
    print("Cookie:", cookie)

time.sleep(10)
driver.quit()

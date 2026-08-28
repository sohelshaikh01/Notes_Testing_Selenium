# A2	Write a working executable code using any programming language like Python, Java, etc using
# Selenium to automate below test steps:
# 1. Open "https://www.wikipedia.org/" in Chrome browser.
# 2. Set the chrome browser window size to width=700, height=600
# 3. Enter "Test Automation" in search textbox
# 4. Press keyboard "Enter" key
# 5. Fetch Page Title value using Selenium and print those in IDE console

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")

# set window size
driver.set_window_size(900, 700)

search_box = driver.find_element(By.XPATH, "//input[@id='searchInput']")
search_box.send_keys("Test Automation")
search_box.send_keys(Keys.ENTER)
time.sleep(2)

print("Page Title:", driver.title)

time.sleep(10)
driver.quit()

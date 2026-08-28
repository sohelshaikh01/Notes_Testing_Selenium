# B2	Write a working executable code using any programming language like Python, Java, etc using
# Selenium to automate below test steps:
# 1. Open "https://www.wikipedia.org/" in Chrome browser.
# 2. Use Explicit wait to check if "The Free Encyclopaedia" text present in DOM
# 3. Enter "Test Automation" in search textbox
# 4. Press keyboard "Enter" key
# 5. Fetch all cookies using Selenium and print those in IDE console.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
time.sleep(2)

# explicit wait to check text
wait = WebDriverWait(driver, 10)

text = None

try:
    text = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'The Free Encyclopaedia')]")
        )
        # EC.text_to_be_present_in_element(By.TAGNAME, "The Free Encyclopaedia")
    )
except:
    print("Text element not found")
    
if text is not None:
    print("Text present in the DOM")
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
# Work on "https://www.google.com"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Make chrome window in maximum
driver.maximize_window()
time.sleep(3)

try:
    textBox = driver.find_element(By.XPATH, "//textarea[@name='q']")
except:
    print("Element not found")

print("Location (x) and (y):", textBox.location)
print("Dimension (Size):", textBox.size)
time.sleep(3)

if textBox.is_displayed():
    print("Textbox is displayed")

if textBox.is_enabled():
    textBox.send_keys("Selenium Automation")
    textBox.send_keys(Keys.ENTER)
    print("Search textbox is Enabled")
else:
    print("Search textbox is disabled")

time.sleep(10)
driver.quit()
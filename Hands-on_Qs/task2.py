# Work on "https://www.facebook.com"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

# Make chrome window in maximum
driver.maximize_window()
time.sleep(3)

try:
    logo = driver.find_element(By.XPATH, "//div[@class='x106a9eq']//*[name()='svg']")
except:
    logo = driver.find_element(By.CLASS_NAME, "x1lliihq x2lah0s x1k90msu x2h7rmj x1qfuztq x1fey0fg xy75621 xni59qk")

print("Location:", logo.location)
print("Size:", logo.size)
time.sleep(3)

if logo.is_displayed() and logo.is_enabled():
    logo.click()
    print("Facebook logo is Clickable")
else:
    print("Facebook logo is not clickable")

time.sleep(10)
driver.quit()
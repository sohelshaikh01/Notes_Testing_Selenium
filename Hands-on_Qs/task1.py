# Work on "https://www.google.com"
# 13-08-2026

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Make chrome window in full screen
driver.fullscreen_window()
time.sleep(3)

try:
    logo = driver.find_element(By.XPATH, '//img[@alt="Google"]')
except:
    logo = driver.find_element(By.CLASS_NAME, "lnXdpd")

# Operation on logo
print("Location:", logo.location)
print("Size:", logo.size)
time.sleep(3)

if logo.is_displayed() or logo.is_enabled():
    logo.click()
    print("Google logo is clickable")
else:
    print("Google logo in not clickable")

time.sleep(10)
driver.quit()

# Work on "https://www.google.com"

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

# Taking logo screenshot
logo.screenshot("google_logo.png")
time.sleep(3)

print("Location:", logo.location)
print("Size:", logo.size)
time.sleep(3)

if logo.is_displayed():
    print("Google logo found")
else:
    print("Google logo not found")

time.sleep(10)
driver.quit()
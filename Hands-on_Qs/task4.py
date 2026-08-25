# Work on "https://www.youtube.com"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

# Make chrome window in maximum
driver.maximize_window()
time.sleep(3)

try:
    logo = driver.find_element(By.XPATH, "//ytd-topbar-logo-renderer[@id='logo']//div[@class='style-scope ytd-topbar-logo-renderer']//div")
except:
    print("Element not found")

print("Location:", logo.location)
print("Size:", logo.size)
time.sleep(3)

if logo.is_displayed():
    print("Youtube logo is displayed")

if logo.is_enabled() or logo.is_clickable():
    logo.click()
    print("Youtube logo is clicked")
else:
    print("Youtube logo is not clicked")

time.sleep(10)
driver.quit()

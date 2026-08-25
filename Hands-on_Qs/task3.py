# Work on "https://www.amazon.com"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

# Make chrome window in maximum
driver.maximize_window()
time.sleep(3)

try:
    searchBox = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
except:
    print("Element not found")

print("Location:", searchBox.location)
print("Dimension (Size):", searchBox.size)
time.sleep(3)

if searchBox.is_enabled():
    searchBox.send_keys("Selenium WebDriver")
    searchBox.send_keys(Keys.ENTER)
    print("Search box is Enabled")
else:
    print("Search box is disabled")

time.sleep(10)
driver.quit()
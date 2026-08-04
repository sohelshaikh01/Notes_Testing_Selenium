# Window & Tab Simulation 1.4 - 29-07-2026
# Create a Window | Tab

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# simulate keyboards keys
import time

driver = webdriver.Chrome()
driver.get("https://www.dev.to")
time.sleep(2)

# Create New Window
driver.switch_to.new_window("window")
driver.get("https://www.facebook.com")
time.sleep(2)

# Create New Tab in present window
driver.switch_to.new_window("tab")
driver.get("https://www.youtube.com")
time.sleep(2)

print("Program Executed Successfully !!!")
time.sleep(10)

driver.close()
driver.quit()
print("Program Ends Successfully !!!")
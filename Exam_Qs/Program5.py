# 1	Write a working executable code using any programming language like Python, Java, etc using
# Selenium to automate below test steps:
# 1. Open "https://www.tata.com/" in Chrome browser.
# 2. Open new Chrome browser window
# 3. Go back to previous window where "https://www.tata.com/" was opened
# 4. Now open new tab and open "https://www.facebook.com/" into it
# 5. Use Explicit Wait and check if total 3 Windows are open or not using Expected Condition
# 6. Close all webdriver sessions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.tata.com/")

win_handler = driver.current_window_handle

# In new window
driver.switch_to.new_window("window")
driver.get("https://www.tata.com")

# Prev window
driver.switch_to.window(win_handler)

# Prev window new tab
driver.switch_to.new_window("tab")
driver.get("https://www.facebook.com/")

wait = WebDriverWait(driver, 10)

result = wait.until(
    EC.number_of_windows_to_be(3)
)

print("Total Tabs opened:", len(driver.window_handles))
print("Result is:", result)

time.sleep(10)
driver.quit()
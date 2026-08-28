# A1	Write a working executable code using any programming language like Python, Java, etc using
# Selenium to automate below test steps:
# 1. Open "https://demoqa.com/text-box" in Chrome browser.
# 2. Enter "Test Automation" into the "Full Name" textbox.
# 3. Enter "test@automation.com" into the "Email" textbox.
# 4. Enter "Pune Maharashtra" into the "Current Address" textarea
# 5. Enter "Pune India" into the "Permanent Address" textarea
# 6. Click the "Submit" button
# 7. The submitted values will be shown below the "Submit" button, fetch those values using
# Selenium and print those in IDE console.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element(By.ID, "userName")
full_name.send_keys("Kyria Anot")

user_email = driver.find_element(By.ID, "userEmail")
user_email.send_keys("superman01@gmail.com")

c_address = driver.find_element(By.ID, "currentAddress")
c_address.send_keys("Shinde pool, pune")

p_address = driver.find_element(By.ID, "permanentAddress")
p_address.send_keys("CF, USA")

time.sleep(2)
submit_btn = driver.find_element(By.ID, "submit")
submit_btn.click()

output = driver.find_element(By.ID, "output")
print(output.text)

time.sleep(10)
driver.quit()
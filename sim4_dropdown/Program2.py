# Radion Buttion 4.2 - 04-08-2026
# --incomplete

# TEXTBOX + RADIO BUTTON #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 10)

create_account_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 
"Create new account")))
create_account_button.click()

# registration_form = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@id='reg']")))

first_name = wait.until(EC.presence_of_element_located((By.ID, "_R_1cl2p4jikacppb6amH1_")))
last_name = wait.until(EC.presence_of_element_located((By.ID, "_R_1kl2p4jikacppb6amH1_")))
mobile_number = wait.until(EC.presence_of_element_located((By.ID, "_R_6ad8p4jikacppb6amH1_")))
password = wait.until(EC.presence_of_element_located((By.ID, "_R_clap4jikacppb6amH1_")))

first_name.send_keys("YourName")
last_name.send_keys("YourSurname")
mobile_number.send_keys("1234567890")
password.send_keys("SecurePassword123")
print("Naming Filled...")
time.sleep(3)

day = wait.until(EC.presence_of_element_located((By.XPATH, "DAY")))
month = wait.until(EC.presence_of_element_located((By.XPATH, "MONTH")))
year = wait.until(EC.presence_of_element_located((By.XPATH, "YEAR")))

day.send_keys("6")
month.send_keys("Sep")
year.send_keys("2000")
print("Date Filled...")
time.sleep(3)

gender_male = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='2']")))
gender_female = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='1']")))
gender_custom = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='-1']")))

gender_male.click()
print("Gender Selected...")
time.sleep(3)

sign_up_button = wait.until(EC.element_to_be_clickable((By.NAME, "websubmit")))
sign_up_button.click()
time.sleep(3)

# Either success/error message handling. Facebook wont accept automated accounts anymore
confirmation_message_wait = WebDriverWait(driver, 120)
confirmation_message = confirmation_message_wait.until(
   EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'confirmation')]"))
)
time.sleep(3)

print("User created successfully.")
driver.quit()

time.sleep(10)
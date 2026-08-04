# Using Dropdown Attribute 3.2 - 31-07-2026
# Most questions asked from Dropdown
# Select and Deselect Methods

from selenium import webdriver # DROPDOWN #
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# Need to import Select class to use Dropdown
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dropdown")

# Dropdown specifications
# mydropdown = driver.find_element(By.ID, "dropdown")
mydropdown = driver.find_element(By.XPATH, "//select[@id='dropdown']")

# To select dropdown we have to pass dropdown web element.
# because of Select class implementation
dropdown = Select(mydropdown)

# Tag will start with <Select> and values comes from <Option>

dropdown.select_by_visible_text("Option 1")
time.sleep(3)

select_option = dropdown.first_selected_option
print(f'Selected option: {select_option.text}')

# Select Option 2 by value
dropdown.select_by_value("2")
time.sleep(3)

# Index starts from 0, here 0th position is default option (Disable Option)
# 0: Default Disabled, 1: Option1, 2: Option2
dropdown.select_by_index(1)
time.sleep(3)

dropdown.deselect_by_visible_text("Option 1") # error ?   
dropdown.deselect_all()        # error ?  

driver.quit()

time.sleep(10)

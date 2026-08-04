# Multi-Select Dropdown 4.1 - 04-08-2026
# Page Start 93

# Dropdown handling can be done by 5 different approaches.

# MULTI-SELECT DROPDOWN #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")

multi_select_element = driver.find_element(By.ID, "cars")   # The ID for Standard multi select
multi_select = Select(multi_select_element)

multi_select.select_by_visible_text("Volvo") # Add time.sleep(5)
time.sleep(3)
multi_select.deselect_by_visible_text("Volvo")
time.sleep(5)

multi_select.select_by_index(1)          # Select "Saab" (index 1)
time.sleep(3)
multi_select.select_by_value("audi")     # Select "Audi"
time.sleep(5)

all_selected_opt_list = multi_select.all_selected_options
for opt in all_selected_opt_list:
    print(opt.text)
time.sleep(3)

multi_select.deselect_by_index(0)
multi_select.deselect_by_value("audi") 
multi_select.deselect_all()

driver.quit()
time.sleep(10)

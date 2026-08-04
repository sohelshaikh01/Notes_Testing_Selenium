# Mouse Simulation 5.1 - 04-08-2026
# Page Start 100

# We need ActionsChain Class
# Mouse is not restricted to any element, so we pass driver in class instead of element

# How we perform right click in mouse ?
# Run the method and pass element
# Execute actions.perform() to perform action

# MOUSE SIMULATION #
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# ActionChains class allow mouse simulation
import time

driver = webdriver.Chrome()
driver.get("https://imcc.mespune.in/")
program_menu = driver.find_element(By.XPATH, "//li[@id='menu-item-4383']")

actions = ActionChains(driver)
actions.move_to_element(program_menu).perform()

time.sleep(5)

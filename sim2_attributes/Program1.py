# Get Attribute 2.1 - 30-07-2026
# Page Start 76

from selenium import webdriver   # WAITS #
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(10)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Pune")

wait = WebDriverWait(driver, 15)
search_box_explicit = wait.until(
   EC.presence_of_element_located((By.NAME, "q"))    
)

search_box_explicit.send_keys("Maharashtra")
polling_wait = WebDriverWait(driver, 20, poll_frequency=3, 
                             
ignored_exceptions=[Exception])

search_box_polling = polling_wait.until(
   EC.visibility_of_element_located((By.NAME, "q"))    
)

search_box_polling.send_keys("India")

driver.quit()

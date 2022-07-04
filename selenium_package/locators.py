from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
full_name = driver.find_element(By.ID, 'Form_submitForm_Name')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
policy_link = driver.find_element(By.LINK_TEXT, 'Privacy Policy')

username_url.send_keys("naveenautomationlabs")
full_name.send_keys("Naveen")
email.send_keys("naveen@gmail.com")
policy_link.click()
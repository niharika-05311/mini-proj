from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/91941/mini-project/notes/selenium-js-login.html")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

result = driver.find_element(By.ID, "result").text

if result == "Login Successful":
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()
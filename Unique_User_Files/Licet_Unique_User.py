import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = input("Enter the URL: ")

driver.get(url)
wait = WebDriverWait(driver, 30)  

def button_interactions(url):
    try:
        # find buttons
        buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button, input[type='button'], input[type='submit'], input[type='reset'], a.btn, a.button")))
        print(f"Found {len(buttons)} buttons.")

        presence_time = (len(buttons) // 2) * 15  # add 15 seconds for every 2 buttons 

        print(f"Total presence time based on button count: {presence_time} seconds")

    except Exception as e:
        print(f"No buttons were found.")

button_interactions(url)
driver.quit()

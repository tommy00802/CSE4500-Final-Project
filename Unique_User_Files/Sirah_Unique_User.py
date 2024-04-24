from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the keyword to search for
keyword = "student"

# Define the URL of the website
url = input ("Enter the URL: ")

# Define the function to recursively check for presence of keyword, images, and links
def check_content(driver):
    # Check if content contains the keyword
    if keyword in driver.page_source:
        # Extend presence time by 10 seconds
        time.sleep(10)
    
    # Check if there are images
    images = driver.find_elements_by_tag_name('img')
    if images:
        # Extend presence time by 10 seconds for every image
        time.sleep(len(images) * 10)
    
    # Check if a link exists
    links = driver.find_elements_by_tag_name('a')
    if links:
        # Extend presence time by 10 seconds and click on the link
        link = links[0]  # Click on the first link found
        link.click()
        # Wait for the new page to load
        WebDriverWait(driver, 10).until(EC.url_changes(url))

        # Recursively check the requirements on the new page
        check_content(driver)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
driver.get(url)

# Call the function to check content recursively
check_content(driver)

# Close the browser
driver.quit()

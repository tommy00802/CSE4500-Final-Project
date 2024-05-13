import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient

# Initialize browser
driver = webdriver.Chrome()

# MongoDB connection string
connection_string = "mongodb+srv://jalton:mtpJrE0zmD7eXzXf@cluster0.bjnrjj9.mongodb.net/Database1"

# Connect to MongoDB
client = MongoClient(connection_string)

# Specify the database and collection
db = client["Database1"]
collection = db["Collection1"]

print("Connected to MongoDB successfully.")

# Navigate to your website 
driver.get("http://localhost:3000/")  

# Track presence time 
presence_time = time.time()

# Track scrolling
scroll_height = driver.execute_script("return document.body.scrollHeight")  
current_scroll = driver.execute_script("return window.pageYOffset")

# Track clicks
buttons = driver.find_elements(By.TAG_NAME, "button")
num_clicks = len(buttons)

# Extract title and paragraph contents
paragraph_texts = [paragraph.text for paragraph in driver.find_elements(By.TAG_NAME, 'p')]
title = driver.title
paragraph = '\n'.join(paragraph_texts)

# Define metric_data
metric_data = {
    "timestamp": time.strftime("%H:%M:%S"),
    "presence_time": presence_time,
    "scrolling_pixels": current_scroll,
    "num_clicks": num_clicks,
    "title": title,
    "paragraph": paragraph
}

try:
    # Print metric_data before insertion
    print("Inserting data into MongoDB:", metric_data)
    collection.insert_one(metric_data)
    print("Data inserted successfully.")
    
    # Wait for a moment to allow the data to be processed by MongoDB
    time.sleep(1)
    
    # Query the collection again after a short delay
    print("Querying collection after insertion:")
    cursor = collection.find()
    for document in cursor:
        print(document)
except Exception as e:
    print("An error occurred while inserting data:", e)

driver.quit()
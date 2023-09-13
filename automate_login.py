import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Declare the URL of the login page
login_url = "https://www.example.com/login"

# Declare the username and password for the login
username = "johndoe"
password = "password"

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(login_url)

# Find the username input field and enter the username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys(username)

# Find the password input field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for the login process to complete
time.sleep(5)

# Check if the user is logged in successfully
if driver.find_element(By.ID, "logged-in"):
    print("Login successful")
else:
    print("Login failed")

# Close the browser
driver.quit()

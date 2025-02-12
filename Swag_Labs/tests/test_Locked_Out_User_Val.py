# tests/test_locked_out_user.py
import time
import sys
from selenium import webdriver
from pages.login_page import LoginPage

sys.stdout.reconfigure(encoding='utf-8')

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Initialize Login Page Object
login_page = LoginPage(driver)

# Test case for locked-out user
time.sleep(5)

# Enter username and password for locked-out user
login_page.enter_username("locked_out_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

# Wait for error message to appear
time.sleep(3)

# Verify the error message for locked-out user
error_message = login_page.get_error_message()
expected_message = "Epic sadface: Sorry, this user has been locked out."

assert error_message == expected_message, f"Test failed! Expected: '{expected_message}', but got: '{error_message}'"

print("Locked-out user validation test passed!")

# Close the browser
driver.quit()

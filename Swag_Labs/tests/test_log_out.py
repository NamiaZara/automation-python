# tests/test_login_logout.py
import time
import sys
from selenium import webdriver
from pages.login_page import LoginPage
from pages.log_out import HomePage

sys.stdout.reconfigure(encoding='utf-8')

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Initialize Page Objects
login_page = LoginPage(driver)
home_page = HomePage(driver)

# Log in to the application
time.sleep(10)
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()
time.sleep(5)

# Log out from the application
home_page.click_menu_button()
time.sleep(5)
home_page.click_logout_button()
time.sleep(5)

# Verify that user is on the login page after logout
login_page_title = home_page.is_login_page_displayed()
assert login_page_title, "Logout failed! User is not on the login page."

print("Logout functionality works correctly!")

# Close the browser
driver.quit()

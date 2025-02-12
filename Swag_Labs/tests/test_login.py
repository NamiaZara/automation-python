# tests/test_login.py
import time
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Create a LoginPage object
    login_page = LoginPage(driver)

    # Perform login with valid credentials
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    time.sleep(5)

    # Verify successful login (Products page should be present)
    assert login_page.verify_successful_login(), "Login failed with valid credentials."
    
    driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Create a LoginPage object
    login_page = LoginPage(driver)

    # Perform login with invalid credentials
    login_page.enter_username("wrong_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login_button()

    time.sleep(5)

    # Check if error message is shown
    error_message = login_page.verify_error_message()
    assert error_message is not None, "Error message not displayed for invalid login."

    if error_message:
        print("Login failed with invalid credentials: " + error_message)
    
    driver.quit()

# Run the tests
if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()

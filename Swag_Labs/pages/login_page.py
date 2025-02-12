# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//*[@id='user-name']")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//*[contains(@class, 'error-message-container')]")
        self.products_page_title = (By.XPATH, "//span[@class='title']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def verify_successful_login(self):
        try:
            self.driver.find_element(*self.products_page_title)
            print("Login successful: Products page is loaded.")
            return True
        except:
            print("Login failed: Products page not found.")
            return False

    def verify_error_message(self):
        try:
            error_msg = self.driver.find_element(*self.error_message)
            return error_msg.text
        except:
            return None
    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message-container").text
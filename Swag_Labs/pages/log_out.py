# pages/home_page.py
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_menu_button(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()

    def click_logout_button(self):
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
     
    def is_login_page_displayed(self):
        return self.driver.find_element(By.CLASS_NAME, "login-box").is_displayed()
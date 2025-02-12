from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = "first-name"
        self.last_name_field = "last-name"
        self.zip_code_field = "postal-code"
        self.continue_button = "continue"
        self.finish_button = "finish"
        self.success_message_xpath = "//h2[contains(text(),'Thank you for your order!')]"
        self.checkout_button_xpath = "//*[@id='checkout']"  # Ensure that the checkout button is correctly identified.

    def enter_shipping_information(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, self.first_name_field).send_keys(first_name)
        self.driver.find_element(By.ID, self.last_name_field).send_keys(last_name)
        self.driver.find_element(By.ID, self.zip_code_field).send_keys(zip_code)
    
    def click_continue(self):
        self.driver.find_element(By.ID, self.continue_button).click()

    def click_finish(self):
        self.driver.find_element(By.ID, self.finish_button).click()

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, self.success_message_xpath).text
    
    def click_checkout(self):
        """Click on the Checkout button."""
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()

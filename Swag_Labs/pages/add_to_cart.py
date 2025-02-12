from selenium.webdriver.common.by import By
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items_xpath = "//div[@class='cart_item']"
        self.cart_icon_xpath = "//*[@id='shopping_cart_container']/a"
        self.continue_shopping_button = "//*[@id='continue-shopping']"
        self.remove_button_backpack = "//*[@id='remove-sauce-labs-backpack']"
        self.remove_button_bike_light = "//*[@id='remove-sauce-labs-bike-light']"
        self.product_names_xpath = ".//div[@class='inventory_item_name']"
        self.checkout_button_xpath = "//*[@id='checkout']"
        
    def add_product_to_cart(self, product_id):
        self.driver.find_element(By.ID, product_id).click()
    
    def open_cart(self):
        self.driver.find_element(By.XPATH, self.cart_icon_xpath).click()
    
    def get_cart_items(self):
        return self.driver.find_elements(By.XPATH, self.cart_items_xpath)
    
    def print_product_names(self):
        cart_items = self.get_cart_items()
        for item in cart_items:
            product_name = item.find_element(By.XPATH, self.product_names_xpath).text
            print(f"Product in cart: {product_name}")
    
    def remove_product_from_cart(self, product_id):
        self.driver.find_element(By.ID, product_id).click()

    def continue_shopping(self):
        self.driver.find_element(By.XPATH, self.continue_shopping_button).click()
    
    def click_checkout_button(self):
        self.driver.find_element(By.XPATH, self.checkout_button_xpath).click()
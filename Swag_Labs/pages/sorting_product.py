# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_data(self):
        # Get product names and prices
        names = [item.text for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        prices = [float(item.text.replace("$", "")) for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")]
        return names, prices

    def select_sorting_option(self, value):
        # Select sorting option from dropdown
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value(value)

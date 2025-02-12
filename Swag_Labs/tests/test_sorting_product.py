# tests/test_sorting.py
import time
import sys
from selenium import webdriver
from pages.login_page import LoginPage
from pages.sorting_product import ProductPage

sys.stdout.reconfigure(encoding='utf-8')

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Initialize Page Objects
login_page = LoginPage(driver)
product_page = ProductPage(driver)

# Pause to allow page to load
time.sleep(5)

# Login to the application
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

time.sleep(5)  # Allow products to load

# Sorting options mapping
sorting_options = {
    "az": "Name (A to Z)",
    "za": "Name (Z to A)",
    "lohi": "Price (Low to High)",
    "hilo": "Price (High to Low)"
}

# Loop through sorting options
for value, label in sorting_options.items():
    print(f" Testing sorting by: {label}")

    # Re-locate the dropdown before selecting (to avoid stale element error)
    product_page.select_sorting_option(value)
    time.sleep(5)  # Wait for sorting to apply

    # Get product data
    names, prices = product_page.get_product_data()

    # Expected sorting order
    if value == "az":
        expected_names = sorted(names)
        assert names == expected_names, f" Sorting by {label} failed!"
    elif value == "za":
        expected_names = sorted(names, reverse=True)
        assert names == expected_names, f" Sorting by {label} failed!"
    elif value == "lohi":
        expected_prices = sorted(prices)
        assert prices == expected_prices, f" Sorting by {label} failed!"
    elif value == "hilo":
        expected_prices = sorted(prices, reverse=True)
        assert prices == expected_prices, f" Sorting by {label} failed!"

    print(f" Sorting by {label} is correct!\n")

# Close the browser
driver.quit()

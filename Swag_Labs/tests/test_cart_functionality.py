import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage  # Assuming LoginPage is in 'pages'
from pages.add_to_cart import CartPage    # Assuming CartPage is in 'pages'

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Initialize Page Objects
login_page = LoginPage(driver)
cart_page = CartPage(driver)

# Step 1: Login to the app
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

# Wait for the page to load
time.sleep(5)

# Step 2: Add multiple products to the cart
# Add first product
cart_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
# Add second product
cart_page.add_product_to_cart("add-to-cart-sauce-labs-bike-light")

# Step 3: Verify the cart badge shows the correct item count (2 items)
cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart_count = int(cart_badge.text) if cart_badge.text else 0

assert cart_count == 2, f"Expected 2 items in the cart, but got {cart_count}"

print(f"Cart badge correctly shows {cart_count} items.")
time.sleep(5)

# Step 4: Remove one item from the cart
# Open the cart
cart_page.open_cart()
time.sleep(2)

# Remove first item (backpack)
cart_page.remove_product_from_cart("remove-sauce-labs-backpack")

# Verify the cart badge updates (1 item)
cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart_count = int(cart_badge.text) if cart_badge.text else 0

assert cart_count == 1, f"Expected 1 item in the cart, but got {cart_count}"

print(f"Cart badge correctly updates to {cart_count} item after removing one product.")

# Close the browser
driver.quit()

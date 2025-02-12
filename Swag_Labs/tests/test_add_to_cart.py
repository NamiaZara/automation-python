import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.add_to_cart import CartPage

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Initialize Page Objects
login_page = LoginPage(driver)
cart_page = CartPage(driver)

# Perform login with valid credentials
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

time.sleep(5)

# Verify successful login (Products page should be present)
assert login_page.verify_successful_login(), "Login failed with valid credentials."

# Add products to the cart
cart_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
cart_page.add_product_to_cart("add-to-cart-sauce-labs-bike-light")
cart_page.open_cart()
time.sleep(3)

# Verify the items in the cart
cart_items = cart_page.get_cart_items()
assert len(cart_items) == 2, f"Expected 2 items in the cart, but found {len(cart_items)} items."

# Optional: Print the product names
cart_page.print_product_names()

# Remove both items from the cart
cart_page.remove_product_from_cart("remove-sauce-labs-backpack")
cart_page.remove_product_from_cart("remove-sauce-labs-bike-light")
time.sleep(2)

# Continue shopping
cart_page.continue_shopping()

# Add products back to the cart
cart_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
cart_page.add_product_to_cart("add-to-cart-sauce-labs-bike-light")
cart_page.open_cart()
time.sleep(3)

# Verify the items in the cart again
cart_items = cart_page.get_cart_items()
assert len(cart_items) == 2, f"Expected 2 items in the cart, but found {len(cart_items)} items."

# Optional: Print the product names again
cart_page.print_product_names()

# Remove both items from the cart again
cart_page.remove_product_from_cart("remove-sauce-labs-backpack")
cart_page.remove_product_from_cart("remove-sauce-labs-bike-light")
time.sleep(2)

# Continue shopping
cart_page.continue_shopping()

# Close the browser
driver.quit()

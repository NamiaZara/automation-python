import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.add_to_cart import CartPage
from pages.checkout_process import CheckoutPage

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Initialize Page Objects
login_page = LoginPage(driver)
cart_page = CartPage(driver)
checkout_page = CheckoutPage(driver)

# Perform login with valid credentials
login_page.enter_username("standard_user")
login_page.enter_password("secret_sauce")
login_page.click_login_button()

# Wait for the Products page to load
time.sleep(5)

# Add products to the cart
cart_page.add_product_to_cart("add-to-cart-sauce-labs-backpack")
cart_page.add_product_to_cart("add-to-cart-sauce-labs-bike-light")
cart_page.open_cart()
time.sleep(3)

# Now, click the checkout button from the CartPage
cart_page.click_checkout_button()  # This should be CartPage's method to open checkout, not CheckoutPage's

# Enter shipping information
checkout_page.enter_shipping_information("John", "Doe", "12345")
checkout_page.click_continue()

# Complete the checkout process
checkout_page.click_finish()
time.sleep(5)

# Verify the success message
success_message = checkout_page.get_success_message()
assert success_message == "Thank you for your order!", f"Expected 'Thank you for your order!' but found {success_message}"

print("Success message verified: 'Thank you for your order!'")

# Close the browser
driver.quit()

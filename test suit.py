import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# set up the browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# login
enter_username = driver.find_element(By.ID, "user-name")
enter_username.send_keys('standard_user')
enter_password = driver.find_element(By.ID, 'password')
enter_password.send_keys('secret_sauce')
click_login_button = driver.find_element(By.ID, "login-button")
click_login_button.click()
time.sleep(2)

# add to cart
back_pack = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div')
back_pack.click()
add_to_cart = driver.find_element(By .ID, 'add-to-cart')
add_to_cart .click()
time.sleep(2)

# cart item
cart_item = driver.find_element(By .XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a/span')
cart_item .click()
time.sleep(2)

# checkout item
checkout_item = driver.find_element(By .ID, 'checkout')
checkout_item .click()
time.sleep(2)

enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname .send_keys('Busola')
enter_lastname = driver.find_element(By.ID, 'last-name')
enter_lastname .send_keys('Olubiyi')
enter_postal_code = driver.find_element(By.ID, 'postal-code')
enter_postal_code .send_keys('23401')
time.sleep(2)

# Continue button
continue_button = driver.find_element(By.ID, 'continue')
continue_button .click()
finish_button = driver.find_element(By.ID, 'finish')
finish_button .click()
time.sleep(2)

# Home button
back_home = driver.find_element(By.ID, 'back-to-products')
back_home .click()
bike_light = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div')
bike_light.click()
time.sleep(2)

# add to cart item
bike_light_add_to_cart = driver.find_element(By .ID, 'add-to-cart')
bike_light_add_to_cart.click()
bike_cart_item = driver.find_element(By .XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
bike_cart_item .click()
time.sleep(2)

# checkout item
bike_checkout_item = driver.find_element(By .ID, 'checkout')
bike_checkout_item .click()
time.sleep(2)

# First name and Last name
enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname .send_keys('Bukky')
enter_lastname = driver.find_element(By.ID, 'last-name')
enter_lastname .send_keys('Olumide')
time.sleep(2)

# postal code
enter_postal_code = driver.find_element(By.ID, 'postal-code')
enter_postal_code .send_keys('23401')
time.sleep(2)

# continue button
bike_continue_button = driver.find_element(By.ID, 'continue')
bike_continue_button .click()
time.sleep(2)

# Finish button
bike_finish_button = driver.find_element(By.ID, 'finish')
bike_finish_button .click()
time.sleep(2)

# Home button
back_home = driver.find_element(By.ID, 'back-to-products')
back_home .click()
bolt_shirt = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a')
bolt_shirt.click()
time.sleep(2)

# add to cart bolt
bolt_shirt_add_to_cart = driver.find_element(By .ID, 'add-to-cart')
bolt_shirt_add_to_cart.click()
time.sleep(2)

# cart item bolt shirt
bolt_shirt_cart_item = driver.find_element(By .XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a/span')
bolt_shirt_cart_item .click()
time.sleep(2)

# checkout bolt shirt
bolt_shirt_checkout_item = driver.find_element(By .ID, 'checkout')
bolt_shirt_checkout_item .click()
time.sleep(2)

# enter first and last name
enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname .send_keys('kunle')
enter_lastname = driver.find_element(By.ID, 'last-name')
enter_lastname .send_keys('Okunuga')
time.sleep(2)

# postal code
enter_postal_code = driver.find_element(By.ID, 'postal-code')
enter_postal_code .send_keys('4444')
time.sleep(2)

# continue button
bolt_shirt_continue_button = driver.find_element(By.ID, 'continue')
bolt_shirt_continue_button .click()
time.sleep(2)

# Finish button
bolt_shirt_finish_button = driver.find_element(By.ID, 'finish')
bolt_shirt_finish_button .click()
time.sleep(2)

# Home button
back_home = driver.find_element(By.ID, 'back-to-products')
back_home .click()
time.sleep(2)

# Fleece shirt
fleece_shirt = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/a/div')
fleece_shirt.click()
time.sleep(2)

# Add to cart fleece
fleece_shirt_add_to_cart = driver.find_element(By .ID, 'add-to-cart')
fleece_shirt_add_to_cart.click()
time.sleep(2)

# Cart item
fleece_shirt_cart_item = driver.find_element(By .XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a/span')
fleece_shirt_cart_item .click()
time.sleep(2)

# Checkout
fleece_shirt_checkout_item = driver.find_element(By .ID, 'checkout')
fleece_shirt_checkout_item .click()
time.sleep(2)

# Enter first name and  last name
enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname .send_keys('Adedayo')
enter_lastname = driver.find_element(By.ID, 'last-name')
enter_lastname .send_keys('Bamidele')
time.sleep(2)

# Enter postal code
enter_postal_code = driver.find_element(By.ID, 'postal-code')
enter_postal_code .send_keys('12345')
time.sleep(2)

# Continue button
fleece_shirt_continue_button = driver.find_element(By.ID, 'continue')
fleece_shirt_continue_button .click()
time.sleep(2)

# Finish button
fleece_shirt_finish_button = driver.find_element(By.ID, 'finish')
fleece_shirt_finish_button .click()
time.sleep(2)

# Back home
back_home = driver.find_element(By.ID, 'back-to-products')
back_home .click()
time.sleep(2)

# OneSis lab
oneSis_lab = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[1]/a/div')
oneSis_lab.click()
time.sleep(2)
# Add to cart
oneSis_lab_add_to_cart = driver.find_element(By .ID, 'add-to-cart')
oneSis_lab_add_to_cart.click()
time.sleep(2)

# Cart item
oneSis_lab_cart_item = driver.find_element(By .XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
oneSis_lab_cart_item .click()
time.sleep(2)

# Checkout
oneSis_lab_checkout_item = driver.find_element(By .ID, 'checkout')
oneSis_lab_checkout_item .click()
time.sleep(2)

# Enter first name andlast name
enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname .send_keys('Dupe')
enter_lastname = driver.find_element(By.ID, 'last-name')
enter_lastname .send_keys('Tayo')
time.sleep(2)

# Enter postal code
enter_postal_code = driver.find_element(By.ID, 'postal-code')
enter_postal_code .send_keys('78967')
time.sleep(2)

# Continue button
oneSis_lab_continue_button = driver.find_element(By.ID, 'continue')
oneSis_lab_continue_button .click()
time.sleep(2)

# Finish button
oneSis_lab_finish_button = driver.find_element(By.ID, 'finish')
oneSis_lab_finish_button .click()
time.sleep(2)

# Back homr
back_home = driver.find_element(By.ID, 'back-to-products')
back_home .click()
time.sleep(2)

# Fleece shirt
fleece_shirt = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/a/div')
fleece_shirt.click()
time.sleep(2)

# Add to cart
fleece_shirt_add_to_cart = driver.find_element(By .ID, 'add-to-cart')
fleece_shirt_add_to_cart.click()
time.sleep(2)

# Cart item
fleece_shirt_cart_item = driver.find_element(By .XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a/span')
fleece_shirt_cart_item .click()
time.sleep(2)

# Checkout
fleece_shirt_checkout_item = driver.find_element(By .ID, 'checkout')
fleece_shirt_checkout_item .click()
time.sleep(2)

# Enter first name and last name
enter_firstname = driver.find_element(By.ID, 'first-name')
enter_firstname .send_keys('Adedayo')
enter_lastname = driver.find_element(By.ID, 'last-name')
enter_lastname .send_keys('Bamidele')
time.sleep(2)

# Enter postal code
enter_postal_code = driver.find_element(By.ID, 'postal-code')
enter_postal_code .send_keys('12345')
time.sleep(2)

# Enter continue button
fleece_shirt_continue_button = driver.find_element(By.ID, 'continue')
fleece_shirt_continue_button .click()
time.sleep(2)

# Enter finish button
fleece_shirt_finish_button = driver.find_element(By.ID, 'finish')
fleece_shirt_finish_button .click()
time.sleep(2)

# Back home
back_home = driver.find_element(By.ID, 'back-to-products')
back_home .click()
time.sleep(2)




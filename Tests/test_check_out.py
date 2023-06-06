import allure
import pytest
from selenium.webdriver.common.by import By

from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage
from Assets.Pages.cart_page import CartPage


@allure.epic('Test Checkout process')
@allure.id(1)
@allure.title("Completing a purchase")
@allure.description('A message of completed order will appear')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_backpack(driver):
    login = Login(driver)
    PP = ProductPage(driver)
    cp = CartPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Adding to cart the sauce backpack'):
        PP.add_to_cart_backpack()
        login.click_on_cart_btn()

    with allure.step('Proceeding to the checkout section and completing the purchase'):
        cp.click_on_checkout_btn()
        cp.insert_first_name()
        cp.insert_last_name()
        cp.insert_zip_code()
        cp.click_on_continue_btn()
        cp.click_on_finish_btn()

    with allure.step('Verifying the URL after completing a purchase'):
        expected_url = 'https://www.saucedemo.com/checkout-complete.html'
        actual_url = driver.current_url
        assert actual_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {actual_url}"



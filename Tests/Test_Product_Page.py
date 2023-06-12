import allure
import pytest
from selenium.webdriver.common.by import By

from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Test Valid Login')
@allure.id(1)
@allure.title("Insert Valid username and password and click login")
@allure.description('Product page will open (by default)')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = Login(driver)
    pp = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

        with allure.step('Verifying the URL after login'):
            expected_url = 'https://www.saucedemo.com/inventory.html'
            actual_url = driver.current_url
            assert actual_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {actual_url}"


@allure.epic('Test add to cart backpack')
@allure.id(2)
@allure.title("Adding to cart a backpack")
@allure.description('Product will be added to the cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_backpack(driver):
    login = Login(driver)
    PP = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Adding to cart the sauce backpack'):
        PP.add_to_cart_backpack()
        login.click_on_cart_btn()

    with allure.step('Verifying the presence of the Sauce Labs Backpack in the cart'):
        expected_item_name = 'Sauce Labs Backpack'
        is_item_in_cart = PP.is_item_in_cart(expected_item_name)
        assert is_item_in_cart, f"{expected_item_name} is not found in the cart"


@allure.epic('Test add to cart Bike Light')
@allure.id(3)
@allure.title("Adding to cart a backpack")
@allure.description('Product will be added to the cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_bike_light(driver):
    login = Login(driver)
    PP = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Adding to cart the sauce Labs Bike Light'):
        PP.add_to_cart_bike_light()

    with allure.step('Verifying the presence of the Sauce Labs Backpack in the cart'):
        expected_item_name = 'Sauce Labs Bike Light'
        is_item_in_cart = PP.is_item_in_cart(expected_item_name)
        assert is_item_in_cart, f"{expected_item_name} is not found in the cart"


@allure.epic('Test add to cart Bolt Shirt')
@allure.id(3)
@allure.title("Adding to cart a backpack")
@allure.description('Product will be added to the cart')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_bike_light(driver):
    login = Login(driver)
    PP = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Adding to cart the sauce Labs Bolt shirt'):
        PP.add_to_cart_BOLT_TSHIRT()

    with allure.step('Verifying the presence of the Sauce Labs Bolt T-shirt in the cart'):
        expected_item_name = 'Sauce Labs Bolt T-Shirt'
        is_item_in_cart = PP.is_item_in_cart(expected_item_name)
        assert is_item_in_cart, f"{expected_item_name} is not found in the cart"


@allure.epic('Test Items filtering by name A-Z')
@allure.id(4)
@allure.title("Clicking the filter option")
@allure.description('Items will be filtered by name')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_bike_light(driver):
    login = Login(driver)
    PP = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Clicking on the filter by name option'):
        PP.filter_items_by_name_A_to_Z()
        assert PP.is_items_sorted_A_to_Z(), "Test failed: Items are not sorted by name A to Z"


@allure.epic('Test Items filtering by Price(High-Low)')
@allure.id(5)
@allure.title("Clicking the filter option")
@allure.description('Items will be filtered by price')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_bike_light(driver):
    login = Login(driver)
    PP = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Clicking on the filter by high to low price option'):
        PP.filter_items_by_price_high_to_low()
        assert PP.is_items_sorted_high_to_low(), "Test failed: Items are not sorted by high to low price"


@allure.epic('Test Items filtering by price(Low-High)')
@allure.id(6)
@allure.title("Clicking the filter option")
@allure.description('Items will be filtered by price')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_bike_light(driver):
    login = Login(driver)
    PP = ProductPage(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Clicking on the filter by low to high price option'):
        PP.filter_items_by_price_low_to_high()
        assert PP.is_items_sorted_by_price_low_to_high(), "Test failed: Items are not sorted by price low to high"



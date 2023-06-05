import allure
import pytest
from Assets.Pages.Commons import Login
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Test Valid Login')
@allure.id(1)
@allure.title("Insert Valid username and password and click login")
@allure.description('Product page will open (by default)')
@allure.severity(allure.severity_level.NORMAL)
def test_valid_login(driver):
    login = Login(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Verifying the URL after login'):
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = driver.current_url
        assert actual_url == expected_url, f"URL mismatch. Expected: {expected_url}, Actual: {actual_url}"


@allure.epic('Test Valid Login')
@allure.id(2)
@allure.title("Insert Invalid username and password and click login")
@allure.description('Error massage will display')
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login(driver):
    login = Login(driver)

    with allure.step('Inserting invalid credentials'):
        login.insert_invalid_user_name()
        login.insert_invalid_password()
        login.click_login()

    with allure.step('Verifying login attempt is unsuccessful'):
        assert login.is_login_page(), "Login attempt was successful. Invalid credentials were accepted."



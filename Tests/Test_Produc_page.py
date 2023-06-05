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

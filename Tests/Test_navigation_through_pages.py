import allure
import pytest
from Assets.Pages.Commons import Login
import time
from Assets.Pages.Product_Page import ProductPage


@allure.epic('Test Navigation to about page')
@allure.id(1)
@allure.title("Log in and click on the about button")
@allure.description('About page will be displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_all_items_page(driver):
    login = Login(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Navigating to all items page'):
        login.click_on_menu_BTN()
        time.sleep(5)
        login.click_on_about_btn()

        current_url = driver.current_url
        allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)


@allure.epic('Test Navigation to all items page')
@allure.id(2)
@allure.title("Log in and click on the all items button")
@allure.description('All items page will be displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_navigation_to_all_items_page(driver):
    login = Login(driver)

    with allure.step('Inserting valid user name and login and click login btn'):
        login.insert_user_name()
        login.insert_password()
        login.click_login()

    with allure.step('Navigating to all items page'):
        login.click_on_menu_BTN()
        time.sleep(5)
        login.click_on_all_items_BTN()

        current_url = driver.current_url
        allure.attach(current_url, name="Current URL", attachment_type=allure.attachment_type.TEXT)

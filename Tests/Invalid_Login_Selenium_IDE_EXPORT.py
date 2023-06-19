# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Assets.Pages.Commons import Login


class TestInvalidLogin():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_invalidLogin(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.set_window_size(1092, 819)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("login_invalid")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("Sauce_secrte")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        error_message = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"error\"]"))
        ).text

        assert "Sorry, this user doesn't exist" in error_message, "Expected error message not found"
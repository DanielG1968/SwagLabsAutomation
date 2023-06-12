import os
import Assets.Pages.Utils as U
from Assets.Pages.Commons import Commons
import pyautogui


class CartPage(Commons):
    CHECK_OUT_BTN = (U.By.CSS_SELECTOR, '#checkout')
    FIRST_NAME = (U.By.CSS_SELECTOR, '#first-name')
    LAST_NAME = (U.By.CSS_SELECTOR, '#last-name')
    ZIP_CODE = (U.By.CSS_SELECTOR, '#postal-code')
    CONTINUE_BTN = (U.By.CSS_SELECTOR, '#continue')
    FINISH_BTN = (U.By.CSS_SELECTOR, '#finish')

    def click_on_checkout_btn(self):
        self.click(self.CHECK_OUT_BTN)

    def insert_first_name(self):
        self.insert(self.FIRST_NAME, 'Mike')

    def insert_last_name(self):
        self.insert(self.LAST_NAME, 'Gold')

    def insert_zip_code(self):
        self.insert(self.ZIP_CODE, '7797780')

    def click_on_continue_btn(self):
        self.click(self.CONTINUE_BTN)

    def click_on_finish_btn(self):
        self.click(self.FINISH_BTN)

    def insert_invalid_first_name(self):
        self.insert(self.FIRST_NAME, '86979')

    def insert_invalid_last_name(self):
        self.insert(self.LAST_NAME, '789466/')

    def insert_invalid_zip_code(self):
        self.insert(self.ZIP_CODE, 'ZIP CODE')

    def is_error_message_displayed(self):
        pass
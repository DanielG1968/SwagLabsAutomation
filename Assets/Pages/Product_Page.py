import os
import Assets.Pages.Utils as U
from Assets.Pages.Commons import Commons
import pyautogui


class ProductPage(Commons):
    add_to_cart_Sauce_labs_backpack = (U.By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_to_cart_Sauce_labs_BIKE_LIGHT = (U.By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_to_cart_Sauce_labs_BOTL_TSHIRT = (U.By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    add_to_cart_Sauce_labs_FLEECE_JACKET = (U.By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
    add_to_cart_Sauce_labs_ONESIE = (U.By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    add_to_cart_Sauce_labs_ALL_THE_THINGS_TSHIRT = (U.By.CSS_SELECTOR,
                                                    '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)')
    REMOVE_PRODUCT_BTN = (U.By.CSS_SELECTOR, '#remove-sauce-labs-backpack')

    # Adding to cart actions

    def add_to_cart_backpack(self):
        self.click(self.add_to_cart_Sauce_labs_backpack)

    def add_to_cart_bike_light(self):
        self.click(self.add_to_cart_Sauce_labs_BIKE_LIGHT)

    def add_to_cart_BOLT_TSHIRT(self):
        self.click(self.add_to_cart_Sauce_labs_BOTL_TSHIRT)

    def add_to_cart_fleece_jacket(self):
        self.click(self.add_to_cart_Sauce_labs_FLEECE_JACKET)

    def add_to_cart_onsie(self):
        self.click(self.add_to_cart_Sauce_labs_ONESIE)

    def add_to_cart_red_tshirt(self):
        self.click(self.add_to_cart_Sauce_labs_ALL_THE_THINGS_TSHIRT)

    # REMOVING AN ITEM

    def click_remove_btn(self):
        self.click(self.REMOVE_PRODUCT_BTN)

    def is_item_in_cart(self, expected_item_name):
        pass

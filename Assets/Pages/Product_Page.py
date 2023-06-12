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
    filter_by_name = (U.By.CSS_SELECTOR, '#header_container > div.header_secondary_container > div > span > select')
    filter_price_high_to_low = (U.By.CSS_SELECTOR, '#header_container > div.header_secondary_container > div > span > '
                                                   'select > option:nth-child(4)')
    filter_price_low_to_high = (U.By.CSS_SELECTOR, '#header_container > div.header_secondary_container > div > span > '
                                                   'select > option:nth-child(3)')
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

    def filter_items_by_name_A_to_Z(self):
        self.click(self.filter_by_name)

    def filter_items_by_price_high_to_low(self):
        self.click(self.filter_price_high_to_low)

    def filter_items_by_price_low_to_high(self):
        self.click(self.filter_price_low_to_high)

    def is_items_sorted_A_to_Z(self):
        pass

    def is_items_sorted_high_to_low(self):
        pass

    def is_items_sorted_low_to_high(self):
        pass

    def is_items_sorted_by_price_low_to_high(self):
        pass

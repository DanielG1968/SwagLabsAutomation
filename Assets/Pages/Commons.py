import Assets.Pages.Utils as U


class Commons(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = U.wdw(self.driver, 10)
        self._qwait = U.wdw(self.driver, 2)

    def wait_for(self, locator):
        return self._wait.until(U.ec.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self._wait.until(U.ec.element_to_be_clickable(locator))

    def wait_for_invisibility(self, locator):
        return self._wait.until(U.ec.invisibility_of_element(locator))

    def quick_wait_for_invisibility(self, locator):
        return self._qwait.until(U.ec.invisibility_of_element(locator))

    def wait_for_window_number_to_change(self, num):
        return self._wait.until(U.ec.number_of_windows_to_be(num))

    def switch_tabs(self, tab_to_switch):
        self.wait_for_window_number_to_change(2)
        for tab in self.driver.window_handles:
            if tab != tab_to_switch:
                self.driver.switch_to.window(tab)
                break

    def wait_for_url_change(self, url):
        return self._wait.until(U.ec.url_to_be(url))

    def clear_department_name(self, locator):
        locator = self.driver.find_element(*locator)
        locator.clear()

    def wait_for_alert(self):
        U.sleep(1)
        return self._wait.until(U.ec.alert_is_present())

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_many(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        temp = self.driver.find_element(*locator)
        return temp.text

    def click(self, locator):
        self.wait_for(locator)
        self.driver.find_element(*locator).click()

    def insert(self, locator, insertion):
        locator = self.driver.find_element(*locator)
        locator.send_keys(insertion)

    def clear(self, locator):
        locator = self.driver.find_element(*locator)
        locator.click()
        locator.send_keys(U.keys.CLEAR)

    def get_class(self, locator):
        locator = self.driver.find_element(*locator)
        class_name = locator.get_attribute('class')
        return class_name

    def get_element_size(self, locator):
        div = self.driver.find_element(*locator)
        amount = list(div.find_elements(U.By.TAG_NAME, 'a'))
        size = len(amount)
        return size

    def get_css(self, locator, value):
        css = self.driver.find_element(*locator)
        val = css.value_of_css_property(value)
        return val

    def upload_image(self, locator, image_path):
        locator = self.driver.find_element(*locator)
        locator.send_keys(image_path)

    def get_element_color(self, locator):
        colour_rgb = Commons(self.driver).get_css(locator, 'background')
        colour_hex = U.Color.from_string(colour_rgb).hex
        return colour_hex

    def get_default_value(self, locator):
        element = self.driver.find_element(*locator)
        default_value = element.get_attribute('defaultValue')
        return default_value

    def get_inner_html(self, locator):
        element = self.driver.find_element(*locator)
        default_value = element.get_attribute('innerHTML')
        return default_value


class Login(Commons):
    # Login locators

    LOGIN_CLICK = (U.By.CSS_SELECTOR, '#login-button')
    USERNAME = (U.By.CSS_SELECTOR, '#user-name')
    PASSWORD = (U.By.CSS_SELECTOR, '#password')

    def insert_user_name(self):
        self.insert(self.USERNAME, 'standard_user')

    def insert_password(self):
        self.insert(self.PASSWORD, 'secret_sauce')

    def insert_invalid_user_name(self):
        self.insert(self.USERNAME, 'Mike123')

    def insert_invalid_password(self):
        self.insert(self.PASSWORD, '789456123')

    def click_login(self):
        self.click(self.LOGIN_CLICK)

    # MENU BTN LOCTOR + ACTION

    Menu_BTN = (U.By.CSS_SELECTOR, '#react-burger-menu-btn')

    def click_on_menu_BTN(self):
        self.click(self.Menu_BTN)

    # CART LOCATORS + ACTIONS

    CART_BTN = (U.By.CSS_SELECTOR, '#shopping_cart_container > a')
    REMOVE_FROM_CART_BTN = (U.By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    CHECK_OUT_BTN = (U.By.CSS_SELECTOR, '#checkout')

    def click_on_cart_btn(self):
        self.click(self.CART_BTN)

    def click_on_checkout_btn(self):
        self.click(self.CHECK_OUT_BTN)

    def click_on_remove_from_cart_btn(self):
        self.click(self.REMOVE_FROM_CART_BTN)

    def get_error_message(self):
        pass

    def is_login_page(self):
        pass

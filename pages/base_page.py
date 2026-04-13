from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def get_text(self, locator, timeout=15):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    def go_to_constructor(self):
        self.click_element(BaseLocators.CONSTRUCTOR_LINK)

    def go_to_order_feed(self):
        self.click_element(BaseLocators.ORDER_FEED_LINK)

    def go_to_personal_account(self):
        self.click_element(BaseLocators.PERSONAL_ACCOUNT_BUTTON)

    def get_current_url(self):
        return self.driver.current_url
    
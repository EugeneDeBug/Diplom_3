from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def is_order_feed_visible(self):
        return self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)

    def get_total_orders(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_COUNTER))

    def get_today_orders(self):
        return int(self.get_text(OrderFeedLocators.TODAY_COUNTER))

    def get_order_numbers_in_progress(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderFeedLocators.ORDER_IN_PROGRESS)
        )
        elements = self.driver.find_elements(*OrderFeedLocators.ORDER_IN_PROGRESS)
        return [el.text.strip().lstrip('0') for el in elements if el.text.strip()]

    def is_total_orders_equal_to(self, expected):
        return self.get_total_orders() == expected

    def is_today_orders_equal_to(self, expected):
        return self.get_today_orders() == expected

    def wait_for_order_in_progress(self, order_number, timeout=15):
        locator = (By.XPATH, f"//ul[contains(@class,'OrderFeed_orderListReady')]//li[contains(@class,'text_type_digits-default') and text()='{order_number}']")
        self.wait_for_element_visible(locator, timeout)

    def wait_for_total_orders_equal_to(self, expected, timeout=30):
        WebDriverWait(self.driver, timeout).until(
        lambda d: self.get_total_orders() == expected,
        message=f"Счётчик 'за всё время' не достиг значения {expected}"
    )

    def wait_for_today_orders_equal_to(self, expected, timeout=30):
        WebDriverWait(self.driver, timeout).until(
        lambda d: self.get_today_orders() == expected,
        message=f"Счётчик 'за сегодня' не достиг значения {expected}"
    )

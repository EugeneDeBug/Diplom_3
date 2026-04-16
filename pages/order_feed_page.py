import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Проверка видимости заголовка 'Лента заказов'")
    def is_order_feed_visible(self):
        return self.wait_for_element_visible(OrderFeedLocators.ORDER_FEED_TITLE)

    @allure.step("Получение значения счётчика 'Выполнено за всё время'")
    def get_total_orders(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_COUNTER))

    @allure.step("Получение значения счётчика 'Выполнено за сегодня'")
    def get_today_orders(self):
        return int(self.get_text(OrderFeedLocators.TODAY_COUNTER))

    @allure.step("Получение списка номеров заказов в разделе 'В работе'")
    def get_order_numbers_in_progress(self):
        self.wait_for_element_presence(OrderFeedLocators.ORDER_IN_PROGRESS, timeout=10)
        elements = self.find_elements(OrderFeedLocators.ORDER_IN_PROGRESS)
        return [el.text.strip().lstrip('0') for el in elements if el.text.strip()]

    @allure.step("Ожидание, что счётчик 'за всё время' станет равным {expected}")
    def wait_for_total_orders_equal_to(self, expected, timeout=30):
        def condition(driver):
            return self.get_total_orders() == expected
        self.wait_for_condition(condition, timeout, message=f"Счётчик 'за всё время' не достиг значения {expected}")

    @allure.step("Ожидание, что счётчик 'за сегодня' станет равным {expected}")
    def wait_for_today_orders_equal_to(self, expected, timeout=30):
        def condition(driver):
            return self.get_today_orders() == expected
        self.wait_for_condition(condition, timeout, message=f"Счётчик 'за сегодня' не достиг значения {expected}")

    @allure.step("Получение текста заголовка ленты заказов")
    def get_order_feed_title_text(self):
        return self.get_text(OrderFeedLocators.ORDER_FEED_TITLE)
    
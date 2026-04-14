from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, '
                                             '"OrderFeed_orderListReady")]/li[contains(@class, '
                                             '"text_type_digits-default")]')

    @staticmethod
    def in_progress_order_locator(order_number):
        """Возвращает локатор для конкретного номера заказа в разделе 'В работе'."""
        return (By.XPATH, f"//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default') and text()='{order_number}']")
    

   
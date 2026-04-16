import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from messages import CONSTRUCTOR_TITLE, ORDER_FEED_TITLE

@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        main_page.go_to_constructor()
        assert main_page.is_constructor_visible()
        assert CONSTRUCTOR_TITLE in main_page.get_constructor_title_text()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.is_order_feed_visible()
        assert ORDER_FEED_TITLE in order_feed_page.get_order_feed_title_text()
        
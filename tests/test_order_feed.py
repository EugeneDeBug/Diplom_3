import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from locators.order_feed_locators import OrderFeedLocators


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_counter_increases_after_new_order(self, driver, authorized_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)

        # Вход
        main_page.go_to_personal_account()
        login_page.login(authorized_user["email"], authorized_user["password"])

        # Запоминаем начальное значение счётчика
        main_page.go_to_order_feed()
        initial_total = order_feed_page.get_total_orders()

        # Создаём заказ
        main_page.go_to_constructor()
        main_page.drag_and_drop_bun_to_constructor()
        main_page.wait_for_bun_counter_equal_to(2)
        main_page.click_order_button()
        main_page.close_order_confirmation_modal()

        # Возвращаемся в ленту и проверяем, что счётчик увеличился
        main_page.go_to_order_feed()
        order_feed_page.wait_for_total_orders_equal_to(initial_total + 1)

        assert order_feed_page.get_total_orders() == initial_total + 1

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_counter_increases_after_new_order(self, driver, authorized_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)

        # Вход
        main_page.go_to_personal_account()
        login_page.login(authorized_user["email"], authorized_user["password"])

        # Запоминаем начальное значение счётчика
        main_page.go_to_order_feed()
        initial_today = order_feed_page.get_today_orders()

        # Создаём заказ
        main_page.go_to_constructor()
        main_page.drag_and_drop_bun_to_constructor()
        main_page.wait_for_bun_counter_equal_to(2)
        main_page.click_order_button()
        main_page.close_order_confirmation_modal()

        # Возвращаемся в ленту и проверяем, что счётчик увеличился
        main_page.go_to_order_feed()
        order_feed_page.wait_for_today_orders_equal_to(initial_today + 1)

        
        assert order_feed_page.get_today_orders() == initial_today + 1

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_progress(self, driver, authorized_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)

        # Вход
        main_page.go_to_personal_account()
        login_page.login(authorized_user["email"], authorized_user["password"])

        # Создаём заказ и получаем его номер
        main_page.drag_and_drop_bun_to_constructor()
        main_page.wait_for_bun_counter_equal_to(2)
        main_page.click_order_button()
        order_number = main_page.get_order_number_from_confirmation()
        main_page.close_order_confirmation_modal()

        # Переходим в ленту заказов
        main_page.go_to_order_feed()

        # Ожидаем появления номера в разделе "В работе"
        locator = OrderFeedLocators.in_progress_order_locator(order_number)
        order_feed_page.wait_for_element_visible(locator, timeout=45)

        # Проверяем, что номер действительно присутствует
        numbers_in_progress = order_feed_page.get_order_numbers_in_progress()
        order_number_clean = order_number.lstrip('0')
        assert order_number_clean in numbers_in_progress, \
            f"Номер {order_number} отсутствует в списке 'В работе'"
        
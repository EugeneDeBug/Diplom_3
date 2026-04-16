import allure
from pages.main_page import MainPage

@allure.feature("Конструктор бургера")
class TestBurgerConstructor:

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, driver, authorized_user):
        main_page = MainPage(driver)
        initial_count = main_page.get_bun_counter()
        main_page.drag_and_drop_bun_to_constructor()
        main_page.wait_for_bun_counter_equal_to(initial_count + 2)
        new_count = main_page.get_bun_counter()
        assert new_count == initial_count + 2
        
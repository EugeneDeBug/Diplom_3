import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage

@allure.feature("Модальное окно ингредиента")
class TestIngredientModal:

    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun_ingredient()
        assert main_page.is_ingredient_modal_opened()
        ingredient_name = main_page.get_ingredient_name_from_modal()
        assert len(ingredient_name) > 0

    @allure.title("Закрытие модального окна по клику на крестик")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_bun_ingredient()
        assert main_page.is_ingredient_modal_opened()
        main_page.close_ingredient_modal()
        WebDriverWait(driver, 5).until_not(
            lambda d: main_page.is_ingredient_modal_opened()
        )
        assert not main_page.is_ingredient_modal_opened()
        
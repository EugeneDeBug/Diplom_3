import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.ingredient_details_locators import IngredientDetailsLocators


class MainPage(BasePage):

    @allure.step("Проверка видимости конструктора")
    def is_constructor_visible(self):
        return self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Клик по ингредиенту булки")
    def click_bun_ingredient(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Получение значения счётчика булки")
    def get_bun_counter(self):
        counter_elem = self.wait_for_element_visible(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter_elem.text) if counter_elem.text else 0

    @allure.step("Перетаскивание булки в конструктор")
    def drag_and_drop_bun_to_constructor(self):
        source = self.wait_for_element_visible(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_DROP_ZONE)

        script = """
        function simulateDragDrop(source, target) {
            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);
            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);
            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);
            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.execute_script(script, source, target)

    @allure.step("Ожидание, что счётчик булки станет равным {expected_count}")
    def wait_for_bun_counter_equal_to(self, expected_count, timeout=10):
        def condition(driver):
            return self.get_bun_counter() == expected_count
        self.wait_for_condition(condition, timeout, message=f"Счётчик булки не стал равен {expected_count}")

    @allure.step("Проверка, открыто ли модальное окно ингредиента")
    def is_ingredient_modal_opened(self):
        try:
            self.wait_for_element_visible(IngredientDetailsLocators.MODAL_TITLE, timeout=5)
            return True
        except:
            return False

    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click_element(IngredientDetailsLocators.CLOSE_BUTTON)
        self.wait_for_condition(lambda d: not self.is_ingredient_modal_opened(), timeout=5)

    @allure.step("Ожидание закрытия модального окна ингредиента")
    def wait_for_ingredient_modal_closed(self, timeout=5):
        self.wait_for_condition(lambda d: not self.is_ingredient_modal_opened(), timeout=timeout)

    @allure.step("Получение названия ингредиента из модального окна")
    def get_ingredient_name_from_modal(self):
        return self.get_text(IngredientDetailsLocators.INGREDIENT_NAME)

    @allure.step("Нажатие на кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.wait_for_condition(
            lambda d: d.find_element(*MainPageLocators.ORDER_BUTTON).get_attribute("disabled") is None,
            timeout=15
        )
        self.click_element(MainPageLocators.ORDER_BUTTON)
        time.sleep(5)   # пауза для появления модального окна

    @allure.step("Получение номера заказа из модального окна подтверждения")
    def get_order_number_from_confirmation(self):
        element = self.wait_for_element_visible(MainPageLocators.ORDER_NUMBER_IN_MODAL, timeout=15)
        return element.text.strip()

    @allure.step("Закрытие модального окна подтверждения заказа кликом по крестику через JS")
    def close_order_confirmation_modal(self):
        self.click_element_by_js(IngredientDetailsLocators.CLOSE_BUTTON)
        self.wait_for_condition(
            lambda d: not self.is_ingredient_modal_opened(),
            timeout=5
        )

    @allure.step("Получение текста заголовка конструктора")
    def get_constructor_title_text(self):
        return self.get_text(MainPageLocators.CONSTRUCTOR_TITLE)
    
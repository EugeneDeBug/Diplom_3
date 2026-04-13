import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.ingredient_details_locators import IngredientDetailsLocators


class MainPage(BasePage):
    def is_constructor_visible(self):
        return self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    def click_bun_ingredient(self):
        self.click_element(MainPageLocators.BUN_INGREDIENT)

    def get_bun_counter(self):
        counter_elem = self.wait_for_element_visible(MainPageLocators.INGREDIENT_COUNTER)
        return int(counter_elem.text) if counter_elem.text else 0

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
        self.driver.execute_script(script, source, target)

    def is_ingredient_modal_opened(self):
        try:
            self.wait_for_element_visible(IngredientDetailsLocators.MODAL_TITLE, timeout=5)
            return True
        except:
            return False

    def close_ingredient_modal(self):
        self.click_element(IngredientDetailsLocators.CLOSE_BUTTON)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(IngredientDetailsLocators.MODAL_TITLE)
        )

    def get_ingredient_name_from_modal(self):
        return self.get_text(IngredientDetailsLocators.INGREDIENT_NAME)

    def click_order_button(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: d.find_element(*MainPageLocators.ORDER_BUTTON).get_attribute("disabled") is None
        )
        self.click_element(MainPageLocators.ORDER_BUTTON)
        time.sleep(5)

    def get_order_number_from_confirmation(self):
        primary_locator = (By.XPATH,
                           "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text_type_digits-large')]")
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(primary_locator)
            )
            order_number = self.driver.find_element(*primary_locator).text.strip()
            if order_number and order_number.isdigit():
                return order_number
        except:
            pass

        fallback_locator = (By.XPATH,
                            "//div[contains(@class, 'Modal_modal')]//*[contains(@class, 'text_type_digits-large')]")
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(fallback_locator)
        )
        order_number = self.driver.find_element(*fallback_locator).text.strip()
        return order_number

    def close_order_confirmation_modal(self):
        self.click_element(IngredientDetailsLocators.CLOSE_BUTTON)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'Modal_modal')]"))
        )

    def is_bun_counter_equal_to(self, expected_count):
        return self.get_bun_counter() == expected_count

    
    def wait_for_bun_counter_equal_to(self, expected_count, timeout=10):
        WebDriverWait(self.driver, timeout).until(
        lambda d: self.get_bun_counter() == expected_count,
        message=f"Счётчик булки не стал равен {expected_count}"
    )
        
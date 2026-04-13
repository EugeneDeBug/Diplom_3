from pages.base_page import BasePage
from locators.ingredient_details_locators import IngredientDetailsLocators

class IngredientDetailsPage(BasePage):
    def get_ingredient_name(self):
        return self.get_text(IngredientDetailsLocators.INGREDIENT_NAME)

    def close_modal(self):
        self.click_element(IngredientDetailsLocators.CLOSE_BUTTON)
        
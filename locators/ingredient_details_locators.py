from selenium.webdriver.common.by import By

class IngredientDetailsLocators:
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_NAME = (By.XPATH, "//h2[contains(@class, 'text_type_main-large')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
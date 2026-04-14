from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUN_INGREDIENT = (By.CSS_SELECTOR, "img[alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, '[class*="counter_counter__"]')
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Оформить заказ']")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__2L34m') and contains(@class, 'text_type_digits-large')]")
    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators

class LoginPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        # Ждём, что страница логина исчезла (появился заголовок конструктора)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        )
        
        from locators.base_locators import BaseLocators
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BaseLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        
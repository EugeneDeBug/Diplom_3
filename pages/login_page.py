import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизация пользователя с email: {email}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_TITLE, timeout=15)
        
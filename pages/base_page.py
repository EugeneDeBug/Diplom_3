import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_for_element_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание присутствия элемента в DOM: {locator}")
    def wait_for_element_presence(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Ожидание, что элемент станет кликабельным: {locator}")
    def wait_for_element_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator, timeout=15):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step("Клик по элементу через JavaScript: {locator}")
    def click_element_by_js(self, locator, timeout=15):
        element = self.wait_for_element_visible(locator, timeout)
        self.execute_script("arguments[0].click();", element)

    @allure.step("Получение текста элемента: {locator}")
    def get_text(self, locator, timeout=15):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def send_keys(self, locator, text, timeout=15):
        element = self.wait_for_element_visible(locator, timeout)
        element.send_keys(text)

    @allure.step("Поиск элементов: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Выполнение JavaScript: {script}")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Ожидание выполнения пользовательского условия")
    def wait_for_condition(self, condition, timeout=15, message=None):
        WebDriverWait(self.driver, timeout).until(condition, message=message)

    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.click_element(BaseLocators.CONSTRUCTOR_LINK)

    @allure.step("Переход в Ленту заказов")
    def go_to_order_feed(self):
        self.click_element(BaseLocators.ORDER_FEED_LINK)

    @allure.step("Переход в Личный кабинет")
    def go_to_personal_account(self):
        self.click_element(BaseLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url
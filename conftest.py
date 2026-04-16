import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helpers.api_helpers import register_user, delete_user
from helpers.data_generators import generate_user_data
from url import BASE_URL

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def authorized_user(driver):
    """
    Создаёт пользователя через API, возвращает словарь с email, password и token.
    После теста удаляет пользователя.
    """
    user_data = generate_user_data()
    resp = register_user(user_data)
    if resp.status_code != 200:
        pytest.fail(f"Не удалось создать пользователя. Статус: {resp.status_code}, тело: {resp.text}")
    token = resp.json().get("accessToken")
    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "token": token
    }
    if token:
        delete_user(token)
        
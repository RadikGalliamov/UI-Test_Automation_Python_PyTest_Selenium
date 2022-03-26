# Общая подготовка перед запуском тестов (методы 'до' и 'после' запуска основных тестов,
# параметры запуска в командной строке)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем параметр запуска тестов в командной строке(выбор браузера, по умолчанию хром, язык)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language browser: ru,en,fr...')


# Запуск браузера
@pytest.fixture(scope="function")  # запускается для каждого теста
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption('language')
    browser = None
    options = Options()
    if browser_name == "chrome":
        browser = webdriver.Chrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

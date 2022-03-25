# Общая подготовка перед запуском тестов (методы 'до' и 'после' запуска основных тестов,
# параметры запуска в командной строке)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем параметр запуска тестов в командной строке(выбор браузера, по умолчанию хром, язык)
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome")
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language browser: ru,en,fr...')


# Запуск браузера
@pytest.fixture(scope="function")  # запускается для каждого теста
def browser(request):
    language = request.config.getoption('language')                                     #
    options = Options()                                                                 # До тестов
    options.add_experimental_option('prefs', {'intl.accept_languages': language})       #
    browser = webdriver.Chrome(options=options)                                         #
    yield browser
    browser.quit()                                                                      # После тестов



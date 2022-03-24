# Общая подготовка перед запуском тестов (методы 'до' и 'после' запуска основных тестов,
# параметры запуска в командной строке)

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# добавляем параметр запуска тестов в командной строке(выбор браузера, по умолчанию хром, языка)
def pytest_addoption(parser):
    # добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome")
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language browser: ru,en,fr...')


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # запускается для каждой функции
def browser(request):
    language = request.config.getoption('language')                                     #
    options = Options()                                                                 # До тестов
    options.add_experimental_option('prefs', {'intl.accept_languages': language})       #
    browser = webdriver.Chrome(options=options)                                         #
    yield browser
    browser.quit()                                                                      # После тестов



# Page Object для главной страницы сайта (Page Object - страница html - объект в тесте)
import pytest

from .base_page import BasePage
from .locators import MainPageLocators


# Создаем класс MainPage для работы с главной страницей (объектом)
# Main Page стан-ся наследником от класса BasePage из файла base_page.py
# таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка
class MainPage(BasePage):
    # Метод проверки наличия страницы логина
    def go_to_login_page(self):
        # локатор берем из базы с локаторами locators.py *-означает что берем пару значений (кортеж)
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # Нам нужно проверить возможность перехода на страницу логина по ссылке в навбаре для каждой из страниц
        # сайта. Предположим, что таких страниц 20, и, значит, у нас есть 20 тестов, использующих метод
        # go_to_login_page класса MainPage. Затем разработчики добавили alert, который вызывается при клике на нужную
        # нам ссылку. Мы увидим, что все 20 тестов упали, так как в методе go_to_login_page нет шага с обработкой
        # alert, следовательно, метод should_be_login_page не сработает. Добавив обработку alert в метод
        # go_to_login_page, мы восстановим работоспособность всех тестов, не меняя самих тестов:
        #  alert = self.browser.switch_to.alert
        #  alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    # Метод проверки ссылки на вхождение слова login
    def should_be_login_link(self):
        # Локатор берем из базы с локаторами locators.py *-означает что берем пару значений (кортеж)
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

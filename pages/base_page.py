# Базовый класс от которого будут наследоваться другие классы
# Базовые методы работы для любой страницы

import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Переносим готовые методы из основной функции __init__
    # в self лежит объект (страница html)
    def open(self):
        self.browser.get(self.url)

    # Метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор).
    # Чтобы перехватывать исключение, нужна конструкция try/except:
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:  # Название исключения
            return False  # элемент не появился, возвращаем ошибку
        return True  # элемент появился, возвращаем успех

    # Элемент не должен появиться
    def is_not_element_present(self, how, what, timeout=4):
        try:
            # Ожидание (по умолчанию 4 секунды), пока элемент не появиться
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True  # элемент не появился, успех
        return False  # элемент появился, ошибка

    # Элемент должен исчезнуть
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Решение задачи в модальном окне
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Гость переходит на страницу логина, со страницы Х
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # Есть ли ссылка на страницу логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Нет ссылки на страницу логина"

    # Найти корзину и кликнуть по ней
    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        basket_btn.click()

    # Проверка пользователь - залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "Значок пользователя не отображается," \
                                                                     " вероятно неавторизованный пользователь"

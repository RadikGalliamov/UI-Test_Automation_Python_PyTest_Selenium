# Базовый класс от которого будут наследоваться другие классы
# Базовые методы работы со страницами (объектами)


import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    # __init__ - базовая функция-конструктор для класса BasePage,
    # позволяет создавать методы класса BasePage
    # Объект BasePage переноситься в аргумент self и далее к нему применяются методы
    # Также в аргументы передаем переменные browser и url, они будут атрибутами класса
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод open открывает нужную страницу в браузере, исп-я метод get
    # переносим готовые методы из основной функции __init__
    # в self лежит объект (страница html)
    def open(self):
        self.browser.get(self.url)

    # Все проверки будем проводить через assert
    # и перехватывать исключения. Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице
    # BasePage, который будет возвращать нам True или False. Воспользуемся неявным ожиданием
    # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10
    # def __init__(self, browser, url, timeout=10):
    # self.browser = browser
    # elf.url = url
    # self.browser.implicitly_wait(timeout)

    # метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд) и что искать (строку-селектор).
    # Чтобы перехватывать исключение, нужна конструкция try/except:
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False  # элемент не появился
        return True  # элемент появился

    # метод - элемент не появился
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True  # элемент не появился

        return False  # элемент появился

    # метод - элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Метод для решения задачи в модальном окне
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

    # гость может перейти на страницу логина со страницы Х
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # есть ли ссылка на страницу логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # найти корзину и клик по ней
    def go_to_basket(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        basket_btn.click()

    # проверка пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

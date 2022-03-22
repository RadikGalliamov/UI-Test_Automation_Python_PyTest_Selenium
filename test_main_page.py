# Тест-кейсы основной страницы


from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
link_login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


# Метод проверки наличия страницы логина (гость) (MainPage)
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


# Метод проверки ссылки на логин (гость) (MainPage)
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # выполняем метод - проверки наличия страницы логина


# Метод корректный ли url адрес ("login" есть в текущем url браузере), (гость) (LoginPage)
def test_guest_can_should_be_login_url(browser):
    page = LoginPage(browser, link_login_page)
    page.open()
    page.should_be_login_url()  # выполняем метод - проверки ссылки на логин


# Метод проверки формы регистрации (гость) (LoginPage)
def test_guest_should_be_register_form(browser):
    page = LoginPage(browser, link_login_page)
    page.open()
    page.should_be_register_form()  # выполняем метод - проверки формы регистрации


# Метод проверки формы логина (user) (LoginPage)
def test_user_should_be_login_form(browser):
    page = LoginPage(browser, link_login_page)
    page.open()
    page.should_be_login_form()  # выполняем метод - проверки формы логина

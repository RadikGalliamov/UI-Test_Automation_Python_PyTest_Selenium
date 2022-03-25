# Тест-кейсы страницы товара
import time
import pytest
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

PRODUCT_PAGE_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209"
HOME_PAGE = "http://selenium1py.pythonanywhere.com/ru/"


# Параметризуем часть тестов меткой login_user
@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    # setup - базовый метод для всех функций класса TestUserAddToBasketFromProductPage, исполняется после базового,
    # класса BasePage, перед следующими функциями ниже. Открыть страницу регистрации,
    # зарегистрировать нового пользователя, проверить, что пользователь залогинен
    def setup(self, browser):
        page = ProductPage(browser, HOME_PAGE)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_register_form()
        login_page.register_new_user(email=str(time.time()) + "@fakemail.ru", password=str(time.time()))
        login_page.should_be_authorized_user()  # Проверить что пользователь залогинен

    # Пользователь не должен видеть сообщение об успешном добавлении товара
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе появилось, но не должно было появиться"

    @pytest.mark.need_review
    # Пользователь может добавить продукт в корзину
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE)
        page.open()
        name = page.write_product_name()
        price = page.write_product_price()
        page.add_product_to_basket()
        page.wait_adding_alerts()  # ожидаем появления модального окна с названием продукта и ценой
        page.check_added_product_name(name)
        page.check_added_product_price(price)


@pytest.mark.need_review
# Гость может добавить один продукт в корзину
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    name = page.write_product_name()
    price = page.write_product_price()
    page.add_product_to_basket()
    page.wait_adding_alerts()
    page.check_added_product_name(name)
    page.check_added_product_price(price)


@pytest.mark.need_review
# Переходим на страницу корзины из страницы продукта, ожидаем сообщение о пустой корзине, гостем
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)  # переход на страницу корзины
    basket_page.should_be_basket_is_empty()


@pytest.mark.need_review
# Можно ли перейти на страницу логина из страницы продукта
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail(reason="нужно починить этот баг")
# Гость не может увидеть успешное сообщение после добавление продукта в корзину (тест падает)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось, но не должно было появиться"


# Проверяем что нет сообщения об успехе
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось, но не должно было появиться"


# Параметризуем тест как ошибочный
@pytest.mark.xfail(reason="нужно починить этот баг")
# Проверяем что нет сообщения об успехе
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось, но не должно было появиться"


# Есть ли ссылка на страницу логина
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE)
    page.open()
    page.should_be_login_link()


# Переходим на страницу корзины из главной страницы, ожидаем сообщение о пустой корзине, под гостем
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, HOME_PAGE)
    page.open()
    page.go_to_basket()  # клик по кнопке корзина для перехода на страницу корзины
    basket_page = BasketPage(browser, browser.current_url)  # переход на страницу корзины
    basket_page.should_be_basket_is_empty()

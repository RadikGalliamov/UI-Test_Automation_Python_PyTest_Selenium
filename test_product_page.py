# Тест-кейсы страницы товара
import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage

link_209 = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209"
link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link_product_promo = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
new_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

""""
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
"""


# class TestUserAddToBasketFromProductPage():
@pytest.mark.skip
# метод - гость добавляет один продукт в корзину
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    name = page.write_product_name()
    price = page.write_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.wait_adding_alerts()
    page.check_added_product_name(name)
    page.check_added_product_price(price)
    page.check_added_product_price_in_top(price)


@pytest.mark.skip
@pytest.mark.xfail(reason="нужно починить этот баг")
# гость не может увидеть успешное сообщение после добавление продукта в корзину (падает)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_209)
    page.open()
    page.add_product_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось, но не должно было появиться"


@pytest.mark.skip
# проверяем что нет сообщения об успехе
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_209)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось, но не должно было появиться"


@pytest.mark.skip
@pytest.mark.xfail(reason="нужно починить этот баг")
# проверяем что нет сообщения об успехе
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_209)
    page.open()
    page.add_product_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Сообщение об успехе появилось, но не должно было появиться"


# есть ли ссылка на страницу логина
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# можно ли перейти на страницу логина из страницы продукта
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


"""
@pytest.mark.need_review
# создать метод
def test_guest_cant_see_product_in_basket_opened_from_product_page()

@pytest.mark.need_review
# создать метод
def test_guest_can_go_to_login_page_from_product_page()

@pytest.mark.need_review
# создать метод
def test_user_can_add_product_to_basket()
    
    
"""

# Page Object для страницы продукта

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Добавить в корзину
    def add_product_to_basket(self):
        add_product_cl_btn = self.browser.find_element(*ProductPageLocators.ADD_PROD_TO_BASKET)
        add_product_cl_btn.click()

    # Записать название продукта
    def write_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    # Записать цену продукта
    def write_product_price(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_text = product_price_text.split()
        product_price = product_price_text[0]
        return product_price

    # Проверка названия продукта добавленного в корзину
    def check_added_product_name(self, name):
        added_name = self.browser.find_element(*ProductPageLocators.PROD_TO_BASKET).text
        assert name == added_name, 'Ошибка имени добавленного продукта в корзину'

    # Проверка цены продукта добавленного в корзину
    def check_added_product_price(self, price):
        added_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        added_price = added_price.split()
        price_in_bask = added_price[0]
        assert price == price_in_bask, 'Ошибка цены добавленного продукта в корзине'

    # Проверка цены продукта в "Всего в корзине: x.x '
    def check_added_product_price_in_top(self, price):
        added_price_in_top = self.browser.find_element(*ProductPageLocators.PRICE_IN_TOP).text
        added_price_in_top = added_price_in_top.split()
        price_in_top = added_price_in_top[3]
        assert price == price_in_top, 'Ошибка цены добавленного продукта в "Всего в корзине: x.x" '

    # Ожидания модального окна с названием продукта и текстом '... был добавлен в вашу корзину'
    def wait_adding_alerts(self):
        WebDriverWait(driver=self.browser, timeout=20).until(
            EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))

    # Сообщение об успешном добавлении в корзину - появляется
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Ошибка сообщение о успешном добавлении продукта в корзину"

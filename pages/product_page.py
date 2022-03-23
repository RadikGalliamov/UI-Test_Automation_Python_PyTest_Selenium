# Page Object для страницы продукта
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # def add_product_to_basket(self):
    #  self.add_product()
    #  self.product_name_match_in_basket()
    #  self.price_in_basket()

    # метод добавить в корзину
    def add_product_to_basket(self):
        add_product_cl_btn = self.browser.find_element(*ProductPageLocators.ADD_PROD_TO_BASKET)
        add_product_cl_btn.click()

    # метод записать название продукта
    def write_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text

    # метод записать цену продукта
    def write_product_price(self):
        product_price_text = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        product_price_text = product_price_text.split()
        product_price = product_price_text[0]
        return product_price

    # метод проверки названия продукта добавленного в корзину
    def check_added_product_name(self, name):
        added_name = self.browser.find_element(*ProductPageLocators.PROD_TO_BASKET).text
        assert name == added_name, 'Ошибка имени добавленного продукта в корзину'

    # метод проверки цены продукта добавленного в корзину
    def check_added_product_price(self, price):
        added_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        added_price = added_price.split()
        price_in_bask = added_price[0]
        assert price == price_in_bask, 'Ошибка цены добавленного продукта в корзине'

    # метод проверки цены продукта в "Всего в корзине: x.x '
    def check_added_product_price_in_top(self, price):
        added_price_in_top = self.browser.find_element(*ProductPageLocators.PRICE_IN_TOP).text
        added_price_in_top = added_price_in_top.split()
        price_in_top = added_price_in_top[3]
        # time.sleep(120)
        assert price == price_in_top, 'Ошибка цены добавленного продукта в "Всего в корзине: x.x" '

    # метод ожидания модального окна с названием продукта и текстом '... был добавлен в вашу корзину'
    def wait_adding_alerts(self):
        WebDriverWait(driver=self.browser, timeout=20).until(
            EC.presence_of_element_located(ProductPageLocators.INNER_ALERTS))

    # метод сообщение об успешном добавлении в корзину появляется
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Ошибка сообщение о успешном добавлении продукта в корзину"


"""  
    # Старый код

    # метод для проверки добавления продукта в корзину
    def add_product_to_basket(self):
        # Собираем данные о цене продукта 
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_product = price_product.text  # Стоимость одного продукта
        # из строки в price_product находим число
        price_product = price_product.split()
        price_prod = price_product[0]
        # Собираем данные о названии продукта 
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product.text  # имя продукта на странице
        print(name_product)
        # Находим элемент добавить в корзину и кликаем, проходим окно с задачей +
        add_prod_to_basket = self.browser.find_element(*ProductPageLocators.ADD_PROD_TO_BASKET)
        add_prod_to_basket.click()
        add_prod_to_basket = self.solve_quiz_and_get_code()
        # time.sleep(1)
        # Находим текст товар был добавлен в вашу корзину 
        prod_to_basket = self.browser.find_element(*ProductPageLocators.PROD_TO_BASKET)
        prod_to_basket_text = prod_to_basket.text  # текст при добавлении продукта
        print(prod_to_basket_text)
        # time.sleep(1)
        assert 'был добавлен в вашу корзину.' in prod_to_basket_text, 'Ошибка добавления продукта в корзину'

        # name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        # name_product = name_product.text  # имя продукта на странице

        prod_to_basket = self.browser.find_element(*ProductPageLocators.PROD_TO_BASKET)
        prod_to_basket = prod_to_basket.text  # текст при успешном добавлении продукта
        print(prod_to_basket)
        assert name_product in prod_to_basket, 'Ошибка имени добавленного продукта в корзину'

        # price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        # price_product = price_product.text  # Стоимость одного продукта
        # из строки в price_product находим число
        # price_prod = [int(num) for num in filter(lambda num: num.isnumeric(), price_product)]
        # print(price_prod)
        # Находим цену продукта в корзине
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket = price_in_basket.text  # Стоимость продукта в корзине
        price_in_basket = price_in_basket.split()
        price_in_bask = price_in_basket[0]
        assert price_prod == price_in_bask, 'Ошибка цены товара в корзине'
"""

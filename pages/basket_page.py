from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # появление сообщения о пустой корзине
    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), \
            "На странице корзины, нет сообщения что корзина пуста"

# Выносим локаторы во внешнюю переменную

from selenium.webdriver.common.by import By


# Каждый класс будет соответствовать каждому классу PageObject:
# class MainPageLocators:



class LoginPageLocators:
    LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "button[name=login_submit]")
    LOGIN_FORM_WELCOME_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")
    REGIST_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGIST_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGIST_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGIST_FORM_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")
    REGIST_WELCOME_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")


class ProductPageLocators:
    ADD_PROD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type=submit]")
    PROD_TO_BASKET = (By.CSS_SELECTOR, "div#messages :nth-child(1) div strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main :nth-child(1)")
    NAME_ADD_PRODUCT = (By.CSS_SELECTOR, "div#messages :nth-child(1) div :nth-child(1)")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main :nth-child(2)")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, "div#messages :nth-child(3) div.alertinner :nth-child(1) :nth-child(1)")
    INNER_ALERTS = (By.CSS_SELECTOR, "div.alertinner")
    PRICE_IN_TOP = (By.CSS_SELECTOR, "div.basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")  # #messages :nth-child(1)


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") не рабочий селектор

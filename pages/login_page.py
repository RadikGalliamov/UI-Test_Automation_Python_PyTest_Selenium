# Page Object для страницы логина/регистрации
import random
from .base_page import BasePage
from .locators import LoginPageLocators


# Создаем класс LoginPage для работы со страницей логином/регистрацией (объектом)
# LoginPage наследует методы базового класса (BasePage)
# В self нах-ся объект - страница логином/регистрацией
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Метод проверки на корректный url адрес (подстрока "login" есть в текущем url браузере)
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Ссылка не содержит слово "login"'

    # Метод проверки формы логина
    def should_be_login_form(self):
        login_form_username = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_USERNAME)
        login_form_username.send_keys('usertest112@mail.ru')
        login_form_password = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_PASSWORD)
        login_form_password.send_keys('UT34567890')
        login_form_button = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_BUTTON)
        login_form_button.click()
        login_form_welcome_text = self.browser.find_element(*LoginPageLocators.LOGIN_FORM_WELCOME_TEXT)
        login_form_welcome_text = login_form_welcome_text.text
        assert "Рады видеть вас снова" == login_form_welcome_text, 'Ошибка тестирования формы логина'

    # Метод проверки формы регистрации
    def should_be_register_form(self):
        regist_form_email = self.browser.find_element(*LoginPageLocators.REGIST_FORM_EMAIL)
        text_random = str(random.randint(10, 999999999999))
        text_email = 'testui@mail.ru'
        text_random_email = text_random + text_email
        regist_form_email.send_keys(text_random_email)
        regist_form_password1 = self.browser.find_element(*LoginPageLocators.REGIST_FORM_PASSWORD1)
        regist_form_password1.send_keys('UT34567890')
        regist_form_password2 = self.browser.find_element(*LoginPageLocators.REGIST_FORM_PASSWORD2)
        regist_form_password2.send_keys('UT34567890')
        regist_form_button = self.browser.find_element(*LoginPageLocators.REGIST_FORM_BUTTON)
        regist_form_button.click()
        regist_welcome_text = self.browser.find_element(*LoginPageLocators.REGIST_WELCOME_TEXT)
        regist_welcome_text = regist_welcome_text.text
        assert "Спасибо за регистрацию!" == regist_welcome_text, 'Ошибка тестирования формы регистрации'

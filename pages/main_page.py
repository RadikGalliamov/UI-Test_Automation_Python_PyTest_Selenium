# Page Object для главной страницы сайта

from .base_page import BasePage


class MainPage(BasePage):
    # В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)




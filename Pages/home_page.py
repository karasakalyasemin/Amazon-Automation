# pages/home_page.py
from .base_page import BasePage
from locators import Locators

class HomePage(BasePage):
    def accept_cookies(self):
        try:
            self.click(*Locators.ACCEPT_COOKIES_BUTTON_LOCATOR)
        except:
            print("Çerez izin düğmesi bulunamadı veya zaten kabul edilmiş olabilir.")

    def search_product(self, product_name):
        search_box = self.find_element(*Locators.SEARCH_LOCATOR)
        search_box.send_keys(product_name)
        self.click(*Locators.SEARCH_BUTTON_LOCATOR)


# pages/product_page.py
from .base_page import BasePage
from locators import Locators

class ProductPage(BasePage):
    def find_product_detail_element(self):
        return self.find_element(*Locators.PRODUCT_DETAIL_LOCATOR)

    def add_to_cart(self):
        self.click(*Locators.ADD_TO_CART_LOCATOR)

    def get_cart_count(self):
        return self.find_element(*Locators.CART_COUNT_LOCATOR).text
    
    def back_page(self):
        self.click(*Locators.BACK_PAGE_LOCATOR)

# pages/search_results_page.py
from .base_page import BasePage
from locators import Locators

class SearchResultsPage(BasePage):
    def go_to_second_page(self):
        self.click(*Locators.SECOND_PAGE_LOCATOR)

    def current_page(self): 
        return self.find_element(*Locators.CURRENT_PAGE_LOCATOR)

    def select_product(self):
        self.clickByIndex(*Locators.PRODUCT_LINK_LOCATOR, index=16)
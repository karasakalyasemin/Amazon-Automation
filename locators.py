# locators.py
from selenium.webdriver.common.by import By

class Locators:
    ACCEPT_COOKIES_BUTTON_LOCATOR = (By.XPATH, "//input[@name='accept' or @value='Accept Cookies']")
    SEARCH_LOCATOR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON_LOCATOR = (By.ID, 'nav-search-submit-button')
    SECOND_PAGE_LOCATOR = (By.CSS_SELECTOR, "a[aria-label='2 sayfasına git']")
    PRODUCT_LINK_LOCATOR = (By.CSS_SELECTOR, "span[class='a-size-base-plus a-color-base a-text-normal']")
    ADD_TO_CART_LOCATOR = (By.ID, 'add-to-cart-button')
    CART_COUNT_LOCATOR = (By.CLASS_NAME, 'a-dropdown-prompt')
    BACK_PAGE_LOCATOR = (By.ID, 'nav-logo-sprites')
    CURRENT_PAGE_LOCATOR = (By.XPATH, "//span[@class='s-pagination-item s-pagination-selected']")
    PRODUCT_DETAIL_LOCATOR = (By.CSS_SELECTOR, "div[class='_p13n-desktop-sims-fbt_fbt-desktop_title-component-wrapper__2CKPJ']")


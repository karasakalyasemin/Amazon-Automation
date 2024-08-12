import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Locators(object):
    ACCEPT_COOKIES_BUTTON_LOCATOR = (By.XPATH, "//input[@name='accept' or @value='Accept Cookies']")
    SEARCH_LOCATOR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON_LOCATOR = (By.ID,'nav-search-submit-button')
    SECOND_PAGE_LOCATOR = (By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[67]/div/div/span/a[1]')
    PRODUCT_LINK_LOCATOR = (By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[25]/div/div/div/div/span/div/div/div[1]/span/a/div/img')
    ADD_TO_CART_LOCATOR = (By.ID,'add-to-cart-button')
    CART_COUNT_LOCATOR = (By.CLASS_NAME, 'a-dropdown-prompt')
    BACK_PAGE_LOCATOR = (By.ID,'nav-logo-sprites')

class Constants:
    BASE_URL ='https://www.amazon.com.tr/'
    SEARCH_KEY = 'samsung'

class TestAmazonSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(Constants.BASE_URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_search_amazon(self):
        
        # 1. Amazon ana sayfasının açıldığını doğrula
        self.assertEqual(Constants.BASE_URL, self.driver.current_url,"Amazon Anasayfa Açılmadı")

        # Çerez izin düğmesini bul ve tıkla
        try:
            ACCEPT_COOKIES_BUTTON= self.driver.find_element(*Locators.ACCEPT_COOKIES_BUTTON_LOCATOR)
            ACCEPT_COOKIES_BUTTON.click()
        except:
            print("Çerez izin düğmesi bulunamadı veya zaten kabul edilmiş olabilir.")
        
        # 2. Arama kutusuna 'samsung' yazıp arama yap
        
    def search_product(self):
        SEARCH_BOX = self.driver.find_element(*Locators.SEARCH_LOCATOR)
        SEARCH_BOX.send_keys(Constants.SEARCH_KEY)
        SEARCH_BUTTON = self.driver.find_element(*Locators.SEARCH_BUTTON_LOCATOR)
        SEARCH_BUTTON.click()

        # Arama sonuçlarının yüklenmesi için bekle
        sleep(1)

        # Arama sonuçlarının 'samsung' içerdiğini doğrula
        self.assertIn(Constants.SEARCH_KEY, self.driver.title.lower())

    def second_page(self):
        # 4. İkinci sayfaya tıklayın ve açıldığını doğrulayın
        SECOND_PAGE_LINK = self.driver.find_element(*Locators.SECOND_PAGE_LOCATOR) 
        SECOND_PAGE_LINK.click()
        sleep(1)
        
    def product_link(self):
        PRODUCT_LINK = self.driver.find_element(*Locators.PRODUCT_LINK_LOCATOR)
        PRODUCT_LINK.click()
        sleep(1)
        
    def add_to_cart(self):
        ADD_TO_CART= self.driver.find_element(*Locators.ADD_TO_CART_LOCATOR)
        ADD_TO_CART.click()
        sleep(3)
        
        self.assertEqual('1', self.driver.find_element(*Locators.CART_COUNT_LOCATOR).text,)
        
    def back_page(self):
        BACK_PAGE = self.driver.find_element(*Locators.BACK_PAGE_LOCATOR)
        BACK_PAGE.click()
        


if __name__ == "__main__":
    unittest.main()
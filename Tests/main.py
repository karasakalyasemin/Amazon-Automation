
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class TestAmazonSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com.tr')
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_search_amazon(self):
        # 1. Amazon ana sayfasının açıldığını doğrula
        self.assertIn("Amazon", self.driver.title)

        # Çerez izin düğmesini bul ve tıkla
        try:
            ACCEPT_COOKIES_BUTTON= self.driver.find_element(By.XPATH, "//input[@name='accept' or @value='Accept Cookies']")
            ACCEPT_COOKIES_BUTTON.click()
        except:
            print("Çerez izin düğmesi bulunamadı veya zaten kabul edilmiş olabilir.")
        
        # 2. Arama kutusuna 'samsung' yazıp arama yap
        SEARCH_BOX = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        SEARCH_BOX.send_keys('samsung')
        SEARCH_BUTTON = self.driver.find_element(By.ID, 'nav-search-submit-button')
        SEARCH_BUTTON.click()

        # Arama sonuçlarının yüklenmesi için bekle
        sleep(1)

        # Arama sonuçlarının 'samsung' içerdiğini doğrula
        self.assertIn('samsung', self.driver.title.lower())

        # 4. İkinci sayfaya tıklayın ve açıldığını doğrulayın
        SECOND_PAGE_LINK =self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[67]/div/div/span/a[1]') 
        SECOND_PAGE_LINK.click()
        sleep(3)
    

        PRODUCT_LINK = self.driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[25]/div/div/div/div/span/div/div/div[1]/span/a/div/img')
        PRODUCT_LINK.click()
        sleep(10)
        
        ADD_TO_CART= self.driver.find_element(By.ID,'add-to-cart-button')
        ADD_TO_CART.click()
        sleep(10)

        CART_COUNT = (By.CLASS_NAME, 'a-dropdown-prompt')
        self.assertEqual('1', self.driver.find_element(*CART_COUNT).text,)

        BACK_PAGE = self.driver.find_element(By.ID,'nav-logo-sprites')
        BACK_PAGE.click()
        


if __name__ == "__main__":
    unittest.main()
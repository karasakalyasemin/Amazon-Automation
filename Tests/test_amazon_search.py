# tests/test_amazon_search.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from constants import Constants
from Pages.home_page import HomePage
from Pages.search_results_page import SearchResultsPage
from Pages.product_page import ProductPage

class TestAmazonSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get(Constants.BASE_URL)
        self.driver.implicitly_wait(5)
        self.home_page = HomePage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_amazon(self):
        # 1. Amazon ana sayfasının açıldığını doğrula
        self.assertEqual(Constants.BASE_URL, self.driver.current_url, "Amazon Anasayfa Açılmadı")

        # Çerez izin düğmesini bul ve tıkla
        self.home_page.accept_cookies()

        # 2. Arama kutusuna 'samsung' yazıp arama yap
        self.home_page.search_product(Constants.SEARCH_KEY)
        sleep(1)

        # Arama sonuçlarının 'samsung' içerdiğini doğrula
        self.assertIn(Constants.SEARCH_KEY, self.driver.title.lower())

        # 4. İkinci sayfaya tıklayın ve açıldığını doğrulayın
        self.search_results_page.go_to_second_page()
        sleep(2)

        # sayfa numarasını kontrol edin
        current_page = self.search_results_page.current_page()
        self.assertEqual(current_page.text, "2")

        # 5. Ürünü seçin
        self.search_results_page.select_product()
        sleep(2)

        # Ürün detay sayfasında olduğunu doğrula
        product_detail_element = self.product_page.find_product_detail_element()
        self.assertEqual(product_detail_element.text, "Sıklıkla Birlikte Alınan Ürünler")
        sleep(2)

        # 6. Sepete ekleyin
        self.product_page.add_to_cart()
        sleep(3)

        # Sepet sayısını doğrulayın
        self.assertEqual('1', self.product_page.get_cart_count())
        
        #7.Anasayfaya geri dönün
        self.product_page.back_page()


if __name__ == "__main__":
    unittest.main()

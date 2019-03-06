from pages import basepage
from pages.Supplier_Pages.pageSignIn import SignIn
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from common.login_buyer import LoginBuyer
from pages.basepage import BasePage
from locators.supplier_locators.add_product_locators import AddProduct
import unittest
from pages.Supplier_Pages.ProductPage import ProductPage


class ProductStatusTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_tab_product(self):
        LoginBuyer().sign_in_existing_supplier(self)
        product = ProductPage(self.driver)
        product.product_tab_click()
        self.wait_for_element(AddProduct.products_link)
        product.add_product()


if __name__ == '__main__':
    unittest.main()
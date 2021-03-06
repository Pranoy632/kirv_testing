import unittest
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

from common.login_buyer import LoginBuyer
from pages.buyer_pages.load_building import BuildLoad
from pages.buyer_pages.search_page import Search
from pages.buyer_pages.logout import Logout


class KirvBuyerTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_buyer(self):
        LoginBuyer().sign_in_existing_buyer(self)
        BuildLoad(self.driver).go_to_categories()
        main_page_category_info = BuildLoad(self.driver).select_any_category()
        details_page_catrgory_info = BuildLoad(self.driver).check_panel()
        print(main_page_category_info, details_page_catrgory_info)
        BuildLoad(self.driver).check_breadcrumb()
        BuildLoad(self.driver).total_of_sub_categories()
        result = BuildLoad(self.driver).check_lowest_first_sorting()
        BuildLoad(self.driver).click_on_sort_by_price()
        BuildLoad(self.driver).sort_by_higher()
        BuildLoad(self.driver).apply_sorting()
        result1 = BuildLoad(self.driver).check_highest_first_sorting()
        BuildLoad(self.driver).click_on_sort_by_price()
        BuildLoad(self.driver).sort_by_lower()
        BuildLoad(self.driver).apply_sorting()
        result2 = BuildLoad(self.driver).check_lowest_first_sorting()
        print(result, result1, result2)

    def test_search(self):
        LoginBuyer().sign_in_existing_buyer(self)
        Search(self.driver).search_blank()
        Search(self.driver).search_invalid_data()
        text_message = Search(self.driver).find_no_results_page()
        self.assertEqual(text_message, 'Products Not Found !!')
        BuildLoad(self.driver).go_to_categories()
        result = Search(self.driver).search_categories_valid()
        print(result)
        Search(self.driver).check_brands_menu_images()
        Search(self.driver).check_brand_numbers()
        check_result = Search(self.driver).search_brand_name()
        self.assertEqual(check_result, 0, 'Result mismatch')

    def test_logout(self):
        LoginBuyer().sign_in_existing_buyer(self)
        logout = Logout(self.driver)
        logout.go_to_logout()


if __name__ == "__main__":
    unittest.main()

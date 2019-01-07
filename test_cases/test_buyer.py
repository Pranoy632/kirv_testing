import unittest
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

from common.login_buyer import LoginBuyer
from pages.buyer_pages.load_building import BuildLoad
from pages.buyer_pages.account import Account


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
        # BuildLoad(self.driver).total_of_sub_categories()
        result = BuildLoad(self.driver).check_lower_sorting()
        BuildLoad(self.driver).click_on_sort_by_price()
        BuildLoad(self.driver).sort_by_higher()
        BuildLoad(self.driver).apply_sorting()
        result1 = BuildLoad(self.driver).check_higher_sorting()
        BuildLoad(self.driver).click_on_sort_by_price()
        BuildLoad(self.driver).sort_by_lower()
        BuildLoad(self.driver).apply_sorting()
        result2 = BuildLoad(self.driver).check_lower_sorting()
        print(result, result1, result2)

        # Account-section
        account = Account(self.driver)
        account.go_to_account()
        account.check_account_active()
        account.check_title_in_account()
        account.go_to_user_profile()
        account.check_user_profile_active()
        account.check_title_on_user_profile()
        account.check_fields()


if __name__ == "__main__":
    unittest.main()

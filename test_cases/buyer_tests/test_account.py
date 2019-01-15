import unittest


from selenium import webdriver
from selenium.webdriver import ChromeOptions

from pages.buyer_pages.account import Account, UserProfile, Brands
from common.login_buyer import LoginBuyer


class KirvBuyerProfileTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def account(self):
        ''' Account section '''

        LoginBuyer().sign_in_existing_buyer(self)
        account = Account(self.driver)
        account.go_to_account()
        account.check_account_active()
        account.check_title_in_account()

    def test_user_profile(self):
        ''' User-profile section '''

        self.account()
        user_profile = UserProfile(self.driver)
        user_profile.go_to_user_profile()
        user_profile.check_user_profile_active()
        user_profile.check_title_on_user_profile()
        user_profile.check_fields()

    def test_brands(self):
        ''' Brands section '''
        self.account()
        brand = Brands(self.driver)
        brand.check_brand_active()
        brand.click_image()


if __name__ == "__main__":
    unittest.main()

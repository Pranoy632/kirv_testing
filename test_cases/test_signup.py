import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

import sys
sys.path.append('../test_pages')

from SignUp_Pages.pageSignup import MainPage
from SignUp_Pages.pageSignUpLogin import SignUpLogin
from SignUp_Pages.pageSignUpContact import SignUpContact
from SignUp_Pages.pageSignUpBrand import SignUpBrand
from SignUp_Pages.pageSignUpCompanyInfo import SignUpCompanyInfo
from SignUp_Pages.pageSignUpLocation import SignUpLocation
from SignUp_Pages.pageSignUpShip import SignUpShipTo
from SignUp_Pages.pageSignUpCategories import SignUpCategories
from SignUp_Pages.pageSignUpVolumes import SignUpVolumes
from SignUp_Pages.pageSignUpCongratulations import SignUpCongratulations


class kirvTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_signUp(self):
        main_page = MainPage(self.driver)
        main_page.click_signup_button()

        signUp_login = SignUpLogin(self.driver)
        signUp_login.fill_email_pwd()
        signUp_login.click_login_signup_button()

        signUp_contactInfo = SignUpContact(self.driver)
        signUp_contactInfo.fill_fields()
        signUp_contactInfo.click_contact_signup_button()

        signUp_brand = SignUpBrand(self.driver)
        signUp_brand.select_checkbox()
        signUp_brand.click_brand_signup_button()

        signUp_companyInfo = SignUpCompanyInfo(self.driver)
        signUp_companyInfo.fill_fields()
        signUp_companyInfo.click_companyInfo_signup_button()

        signUp_location = SignUpLocation(self.driver)
        signUp_location.fill_fields()
        signUp_location.click_location_signup_button()

        signUp_ship = SignUpShipTo(self.driver)
        signUp_ship.fill_fields()
        signUp_ship.click_ship_signup_button()

        signUp_categories = SignUpCategories(self.driver)
        signUp_categories.fill_fields()
        signUp_categories.click_categories_signup_button()

        signUp_volumes = SignUpVolumes(self.driver)
        signUp_volumes.fill_fields()
        signUp_volumes.click_volumes_signup_button()

        signUp_congratulation = SignUpCongratulations(self.driver)
        signUp_congratulation.click_modal_close_btn()


if __name__ == "__main__":
    unittest.main()

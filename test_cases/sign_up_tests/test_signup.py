import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# import sys
# sys.path.append('../pages')

from pages.SignUp_Pages.pageSignup import MainPage
from pages.SignUp_Pages.pageSignUpLogin import SignUpLogin
from pages.SignUp_Pages.pageSignUpContact import SignUpContact
from pages.SignUp_Pages.pageSignUpBrand import SignUpBrand
from pages.SignUp_Pages.pageSignUpCompanyInfo import SignUpCompanyInfo
from pages.SignUp_Pages.pageSignUpLocation import SignUpLocation
from pages.SignUp_Pages.pageSignUpShip import SignUpShipTo
from pages.SignUp_Pages.pageSignUpCategories import SignUpCategories
from pages.SignUp_Pages.pageSignUpVolumes import SignUpVolumes
from pages.SignUp_Pages.pageSignUpCongratulations import SignUpCongratulations


class kirvSignupTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_signUp(self):
        main_page = MainPage(self.driver)
        main_page.click_signup_button()

        # SignUp-login

        signUp_login = SignUpLogin(self.driver)
        signUp_login.title_check()
        signUp_login.login_with_blank_pwd()
        signUp_login.click_login_signup_button()
        try:
            assert signUp_login.login_pwd_error_displayed() == True
            print("Success: signup login password blank error found.")
        except:
            print("No results found for blank password.")
        signUp_login.clear_data()

        signUp_login.login_with_invalid_email()
        signUp_login.click_login_signup_button()
        try:
            assert signUp_login.login_email_error_displayed() == True
            print("Success: signup login email invalid error found.")
        except:
            print("No results found for invalid email.")
        signUp_login.clear_data()

        signUp_login.login_with_blank_email()
        signUp_login.click_login_signup_button()
        try:
            assert signUp_login.login_email_error_displayed() == True
            print("Success: signup login email blank error found.")
        except:
            print("No results found for blank email.")
        signUp_login.clear_data()

        signUp_login.fill_email_pwd()
        signUp_login.click_login_signup_button()

        # contactInfo

        signUp_contactInfo = SignUpContact(self.driver)
        signUp_contactInfo.title_check()
        signUp_contactInfo.fill_fields()

        # Brand

        signUp_brand = SignUpBrand(self.driver)
        signUp_brand.title_check()
        signUp_brand.select_checkbox()
        signUp_brand.click_brand_signup_button()

        # companyInfo

        signUp_companyInfo = SignUpCompanyInfo(self.driver)
        signUp_companyInfo.step_check()
        signUp_companyInfo.title_check()
        signUp_companyInfo.fill_fields()

        # location

        signUp_location = SignUpLocation(self.driver)
        signUp_location.step_check()
        signUp_location.title_check()
        signUp_location.fill_fields()

        # warehouse/ship

        signUp_ship = SignUpShipTo(self.driver)
        signUp_ship.step_check()
        signUp_ship.title_check()
        signUp_ship.fill_fields()

        # categories

        signUp_categories = SignUpCategories(self.driver)
        signUp_categories.step_check()
        signUp_categories.title_check()
        signUp_categories.fill_fields()

        # volumes

        signUp_volumes = SignUpVolumes(self.driver)
        signUp_volumes.step_check()
        signUp_volumes.title_check()
        signUp_volumes.fill_fields()

        # congratulation

        signUp_congratulation = SignUpCongratulations(self.driver)
        signUp_congratulation.check_img_title()
        signUp_congratulation.click_modal_close_btn()

        # email check
        '''
        email_chk = EmailCheck()
        try:
            i = 1
            while i < 10:
                email_chk.email_check()
                time.sleep(5)
                i = i + 1
        except:
            print("No email found")
        '''
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

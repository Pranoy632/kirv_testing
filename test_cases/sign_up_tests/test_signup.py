# import sys
# sys.path.append('../pages')

import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


from pages.signup_pages.sign_up_here import SignUpHere
from pages.signup_pages.sign_up_to_buy import SignUpToBuy
from pages.signup_pages.create_account import CreateAccount
from pages.signup_pages.contact_info import ContactInfo


class kirvSignupTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    def test_signUp(self):

        # signup-link
        main_page = SignUpHere(self.driver)
        main_page.click_signup_link()

        # sign-up-to-buy
        signup_to_buy = SignUpToBuy(self.driver)
        signup_to_buy.page_elements()

        # create account
        create_acct = CreateAccount(self.driver)
        create_acct.create_account_page_elements()

        # contact_info
        contact_info = ContactInfo(self.driver)
        contact_info.contact_info_page_element()
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

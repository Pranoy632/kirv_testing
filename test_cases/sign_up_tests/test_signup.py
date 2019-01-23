# import sys
# sys.path.append('../pages')

import unittest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


from pages.signup_pages.sign_up_here import SignUpHere
from pages.signup_pages.sign_up_to_buy import SignUpToBuy
from pages.signup_pages.create_account import CreateAccount
from pages.signup_pages.contact_info import ContactInfo
from pages.signup_pages.company_info import CompanyInfo
from pages.signup_pages.location import Location
from pages.signup_pages.warehouse import WareHouse
from pages.signup_pages.categories import Categories
from pages.signup_pages.volumes import Volumes
from pages.signup_pages.acknowledgement import Acknowledgement
from pages.signup_pages.congratulations import Cogratulations


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

        # company-info
        company_info = CompanyInfo(self.driver)
        company_info.company_info_page_element()

        # location
        loc = Location(self.driver)
        loc.element_in_location_page()

        # warehouse
        warehouse = WareHouse(self.driver)
        warehouse.elements_of_warehouse()

        # categories
        categories = Categories(self.driver)
        categories.elements_of_categories()
        categories.fill_fields()

        # volumes
        volume = Volumes(self.driver)
        volume.check_element_in_volumes_page()
        volume.fill_fields()

        # acknowledgement
        acknowledge = Acknowledgement(self.driver)
        acknowledge.check_elements_in_acknowledgement()

        # congrats = Cogratulations(self.driver)
        # congrats.check_elements_in_congratulation_page()

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
        # self.driver.close()


if __name__ == "__main__":
    unittest.main()

from pages.basepage import *
from locators.sign_up_locators.locatorSignup import SignupPageLocators


class SignUpToBuy(BasePage):

    def check_kirv_image(self):
        return self.driver.find_element(*SignupPageLocators.kirv_logo).is_displayed()

    def check_title_business_look(self):
        return self.driver.find_element(*SignupPageLocators.business_looking).text

    def check_cart_plus_icon(self):
        return self.driver.find_element(*SignupPageLocators.cart_plus_icon).is_displayed()

    def check_remanufactured_header(self):
        return self.driver.find_element(*SignupPageLocators.buy_remanufactured_product).text

    def check_purchase_remanufactured_para(self):
        return self.driver.find_element(*SignupPageLocators.purchase_remanufactured_products_para).text

    def click_signup_to_buy_btn(self):
        self.driver.find_element(
            *SignupPageLocators.signup_to_buy_btn).click()

    def page_elements(self):
        try:
            assert self.check_kirv_image() == True
        except:
            print("No result found for kirv image.")

        try:
            assert self.check_title_business_look(
            ) == "What type of business are you looking to do with us?"
        except:
            print("No result found for Business look title.")

        try:
            assert self.check_cart_plus_icon() == True
        except:
            print("No result found for cart_plus_icon.")

        try:
            assert self.check_remanufactured_header(
            ) == "I would like to buy remanufactured products from Kirv"
        except:
            print("No result found Remanufactured products header.")

        try:
            assert self.check_purchase_remanufactured_para(
            ) == "Select this option if you’re a retailer that wants to purchase remanufactured products directly from Kirv."
        except:
            print("No result found for purchase remanufactured para")

        self.click_signup_to_buy_btn()

import sys
sys.path.append('../test_locators')
import time

from Basepage import BasePage

from Buyer_Locators.locatorBuyer import BuyerPageLocators


class MainSigninPage(BasePage):

    def check_signin_img(self):
        sigin_img = self.driver.find_element(
            *BuyerPageLocators.signin_kirv_image)
        return sigin_img.is_displayed()

    def check_signin_title(self):
        signin_title = self.driver.find_element(
            *BuyerPageLocators.signin_title)
        return signin_title.is_displayed()

    def email_error(self):
        email_er = self.driver.find_element(
            *BuyerPageLocators.email_login_error)
        return email_er.is_displayed()

    def pwd_error(self):
        pwd_er = self.driver.find_element(*BuyerPageLocators.pwd_login_error)
        return pwd_er.is_displayed()

    def fill_fields(self):
        self.wait_for_element(
            BuyerPageLocators.email_login)

        email_input = self.driver.find_element(
            *BuyerPageLocators.email_login)
        email_input.send_keys("amztest18+20181010142126@gmail.com")

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.pwd_error() == True
            print("Success: signin password blank error found.")
        except:
            print("No result found for blank password.")

        pwd_input = self.driver.find_element(
            *BuyerPageLocators.pwd_login)
        pwd_input.send_keys("amz")

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.pwd_error() == True
            print("Success: signin password incorrect error found.")
        except:
            print("No result found for incorrect password.")

        email_input.clear()
        email_input.send_keys("amz.com")

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.email_error() == True
            print("Success: signin email invalid error found.")
        except:
            print("No result found for invalid email.")

        email_input.clear()

        pwd_input.clear()
        pwd_input.send_keys("amazatic")

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.email_error() == True
            print("Success: signin email blank error found.")

        except:
            print("No result found for blank email.")

        email_input.send_keys("amztest18+20181010142126@gmail.com")
        self.click_signin_btn()

    def click_signin_btn(self):
        signin_btn = self.driver.find_element(
            *BuyerPageLocators.signin_login_btn)
        signin_btn.click()

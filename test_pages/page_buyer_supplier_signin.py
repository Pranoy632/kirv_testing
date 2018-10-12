import sys
sys.path.append('../test_locators')
import time


from Basepage import BasePage

from signin_buyer_supplier_locator import SigInLocators


class MainSigninPage(BasePage):

    def check_signin_img(self):
        sigin_img = self.driver.find_element(
            *SigInLocators.signin_kirv_image)
        return sigin_img.is_displayed()

    def check_signin_title(self):
        signin_title = self.driver.find_element(
            *SigInLocators.signin_title)
        return signin_title.is_displayed()

    def email_error(self):
        email_er = self.driver.find_element(
            *SigInLocators.email_login_error)
        return email_er.is_displayed()

    def pwd_error(self):
        pwd_er = self.driver.find_element(*SigInLocators.pwd_login_error)
        return pwd_er.is_displayed()

    def fill_fields(self, username, password):

        try:
            assert self.check_signin_img() == True
            print("Success: signin Kirv image found.")
        except:
            print("No result for kirv image.")

        try:
            assert self.check_signin_title() == True
            print("Success: signin sign-In title found.")
        except:
            print("No result found for kirv title.")

        self.wait_for_element(
            SigInLocators.email_login)

        email_input = self.driver.find_element(
            *SigInLocators.email_login)
        email_input.send_keys(username)

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.pwd_error() == True
            print("Success: signin password blank error found.")
        except:
            print("No result found for blank password.")

        pwd_input = self.driver.find_element(
            *SigInLocators.pwd_login)
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
        pwd_input.send_keys(password)

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.email_error() == True
            print("Success: signin email blank error found.")

        except:
            print("No result found for blank email.")

        email_input.send_keys(username)
        self.click_signin_btn()

    def click_signin_btn(self):
        signin_btn = self.driver.find_element(
            *SigInLocators.signin_login_btn)
        signin_btn.click()

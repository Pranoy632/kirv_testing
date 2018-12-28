#import sys
#sys.path.append('../locators')
import time


from pages.basepage import BasePage

from locators.sign_in_page_locators.signin_buyer_supplier_locator import SignInLocators


class MainSigninPage(BasePage):

    def check_signin_img(self):
        sigin_img = self.driver.find_element(
            *SignInLocators.signin_kirv_image)
        return sigin_img.is_displayed()

    def check_signin_title(self):
        signin_title = self.driver.find_element(
            *SignInLocators.signin_title)
        return signin_title.is_displayed()

    def check_signup_title(self):
        signUp_title = self.driver.find_element(
            *SignInLocators.signup_title)
        return signUp_title.is_displayed()

    def email_blank_error(self):
        email_er = self.driver.find_element(
            *SignInLocators.email_login_blank_error)
        return email_er.is_displayed()

    def pwd_blank_error(self):
        pwd_er = self.driver.find_element(
            *SignInLocators.pwd_login_blank_error)
        return pwd_er.is_displayed()

    def email_pwd_error(self):
        email_pwd = self.driver.find_element(
            *SignInLocators.email_password_incorrect)
        return email_pwd.is_displayed()

    def fill_fields(self, username, password):

        try:
            assert self.check_signin_img() == True
            print("Success: Kirv image found.")
        except:
            print("No result for kirv image.")

        try:
            assert self.check_signin_title() == True
            print("Success: sign in title found.")
        except:
            print("No result found for kirv title.")

        try:
            assert self.check_signup_title() == True
            print("Success: sign-up title found.")
        except:
            print("No result found for kirv sign-up title.")

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.pwd_blank_error() == True
            print("Success: password blank error found.")
        except:
            print("No result found for blank password.")

        try:
            assert self.email_blank_error() == True
            print("Success: email blank error found.")
        except:
            print("No result found for blank email.")

        self.wait_for_element(
            SignInLocators.email_login)

        email_input_1 = self.driver.find_element(
            *SignInLocators.email_login)
        email_input_1.send_keys(username)

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.pwd_blank_error() == True
            print("Success: signin password blank error found.")
        except:
            print("No result found for blank password.")

        pwd_input_1 = self.driver.find_element(
            *SignInLocators.pwd_login)
        pwd_input_1.send_keys(password)

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.email_blank_error() == True
            print("Success: signin email blank error found.")
        except:
            print("No result found for blank email.")

        email_input_2 = self.driver.find_element(
            *SignInLocators.email_login)
        email_input_2.send_keys("amz@amz.com")

        pwd_input_2 = self.driver.find_element(
            *SignInLocators.pwd_login)
        pwd_input_2.send_keys(password)

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.email_pwd_error() == True
            print("Success: sigin email incorrect found.")
        except:
            print("No result found for incorrect email.")

        email_input_3 = self.driver.find_element(
            *SignInLocators.email_login)
        email_input_3.send_keys(username)

        pwd_input_3 = self.driver.find_element(
            *SignInLocators.pwd_login)
        pwd_input_3.send_keys("amz")

        self.click_signin_btn()
        time.sleep(1)

        try:
            assert self.email_pwd_error() == True
            print("Success: sigin password incorrect found.")
        except:
            print("No result found for incorrect password.")

        email_input_4 = self.driver.find_element(
            *SignInLocators.email_login)
        email_input_4.send_keys(username)

        pwd_input_4 = self.driver.find_element(
            *SignInLocators.pwd_login)
        pwd_input_4.send_keys(password)

        self.click_signin_btn()
        time.sleep(1)

        # try:
        #     assert self.pwd_error() == True
        #     print("Success: signin password incorrect error found.")
        # except:
        #     print("No result found for incorrect password.")

        # email_input.clear()
        # email_input.send_keys("amz.com")

        # self.click_signin_btn()
        # time.sleep(1)

        # try:
        #     assert self.email_error() == True
        #     print("Success: signin email invalid error found.")
        # except:
        #     print("No result found for invalid email.")

        # email_input.clear()

        # pwd_input.clear()
        # pwd_input.send_keys(password)

        # self.click_signin_btn()
        # time.sleep(1)

        # try:
        #     assert self.email_error() == True
        #     print("Success: signin email blank error found.")

        # except:
        #     print("No result found for blank email.")

        # email_input.send_keys(username)
        # self.click_signin_btn()

    def click_signin_btn(self):
        signin_btn = self.driver.find_element(
            *SignInLocators.signin_login_btn)
        signin_btn.click()

import sys
sys.path.append('../test_locators')


from .Basepage import BasePage, fake
from SignUp_Locators.locatorSignup import SigninPageLocators


class SignUpContact(BasePage):

    def fill_fields(self):

        self.wait_for_element(
            SigninPageLocators.contactInfo_signUp_companyName)

        input_companyName = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_companyName)
        input_companyName.send_keys(fake.company())

        input_contactName = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_contactName)
        input_contactName.send_keys(fake.name())

        input_phn = self.driver.find_element(
            *SigninPageLocators.contactInfo_signUp_phn)
        input_phn.send_keys("12345678901")

    def click_contact_signup_button(self):
        element_contact_signup = self.driver.find_element(
            *SigninPageLocators.signup)
        element_contact_signup.click()

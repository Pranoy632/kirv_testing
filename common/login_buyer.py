from pages.buyer_pages.login import Login


class LoginBuyer:

    @staticmethod
    def sign_in_existing_buyer(self):
        Login(self.driver).enter_credentials_existing_buyer()
        Login(self.driver).click_sign_in_button()
        Login(self.driver).wait_for_home_page()

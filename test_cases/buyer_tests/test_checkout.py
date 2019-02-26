import pytest

import allure
from allure_commons.types import AttachmentType

from selenium import webdriver
from selenium.webdriver import ChromeOptions

from pages.buyer_pages.checkout_page import Checkout
from common.login_buyer import LoginBuyer


# def error_screenshot(func):
#     def wrapper(*args, **kwargs):
#         try:
#            func(*args, **kwargs)
#         except AssertionError:
#             allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
#             raise
#     return wrapper

@pytest.fixture()
def setup(request):
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.instance.driver = driver
    driver.get("http://kirv-ui-staging.herokuapp.com/signin")

    yield driver
    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)


@pytest.mark.usefixtures("setup")
class TestCheckout:

    def test_checkout(self):
        LoginBuyer().sign_in_existing_buyer(self)
        Checkout(self.driver).get_each_category()

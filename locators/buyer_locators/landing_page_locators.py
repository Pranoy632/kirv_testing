from selenium.webdriver.common.by import By


class LoginLocators:
    email = (By.NAME, 'username')
    password = (By.NAME, 'password')
    sign_in = (By.CSS_SELECTOR, 'body > div > form > button')
    sign_in_kirv_image = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > div.logo > img')

    sign_in_title = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > h1')

    email_login = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > form > fieldset > field:nth-child(1) > div > label > input')

    pwd_login = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > form > fieldset > field:nth-child(2) > div > label > input')

    email_login_error = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > form > fieldset > field:nth-child(1) > div > span')

    pwd_login_error = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > form > fieldset > field:nth-child(2) > div > span')

    sign_in_login_btn = (
        By.CSS_SELECTOR,
        'ng-component > div.container-fluid > div > div:nth-child(1) > div > form > fieldset > button')



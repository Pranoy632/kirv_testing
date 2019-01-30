from selenium.webdriver.common.by import By


class SignInLocators(object):

    # signIn

    signin_kirv_image = (
        By.XPATH, '//*[@class="logo"]')

    signin_title = (
        By.XPATH, '//*[@class="text-center"]')

    signup_title = (
        By.CSS_SELECTOR, 'div > p')
    #email_login = ( By.CSS_SELECTOR, 'div > div:nth-child(1) > div > form > input:nth-child(3)')
    email_login = (
        By.XPATH, '//label[text()="Email address"]/following-sibling::input')

    #pwd_login = (By.CSS_SELECTOR, 'ng-component > div.container-fluid > div > div:nth-child(1) > div > form > fieldset > field:nth-child(2) > div > label > input')
    pwd_login = (
        By.XPATH, '//label[text()="Password"]/following-sibling::input')

    # email_login_error = (
    #     By.CSS_SELECTOR, 'div > div:nth-child(3)')

    # pwd_login_error = (
    #     By.CSS_SELECTOR, 'div > div:nth-child(4)')

    email_login_blank_error = (
        By.XPATH, '//*[contains(text(),"Please enter your username")]')

    pwd_login_blank_error = (
        By.XPATH, '//*[contains(text(),"Please enter your password")]')

    email_password_incorrect = (
        By.XPATH, '//*[contains(text(),"The username or password is not correct")]')

    signin_login_btn = (By.CLASS_NAME, 'btn-primary')

    ############ Chat popup locators ###########
    chat = (By.TAG_NAME, 'iframe')

    close_chat = (By.XPATH, '//*[@id="root"]/div/div[2]/button')

    close_chat1 = (By.CSS_SELECTOR, '#root > div > div._30us5AS2WYfPMXSfbW1-5E > span > div:nth-child(2) > div > div > div._3rFYHyeAg3meOhdz2al1n- > div.nU8iBIlb3Pnpdfah8T0xS > div._1t1gRyGlfXe220eYtsZnFt')

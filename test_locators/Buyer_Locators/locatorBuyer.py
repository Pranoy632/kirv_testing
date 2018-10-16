from selenium.webdriver.common.by import By


class BuyerPageLocators(object):

    # Header

    kirv_image = (
        By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-xl-1.col-lg-2.col-md-2.col-sm-3.col-4 > span > a > img')

    categories_label = (By.XPATH, '//a[@id="navDropDown-1"]')

    brand_label = (By.XPATH, '//a[@id="navDropDown-2"]')

    search_input = (By.XPATH, '//input[@name="search"]')

    search_btn = (
        By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-xl-4.col-lg-5.col-md-5.col-12.search-box-m > form > button')

    load_label = (By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-auto.ml-auto.d-none.d-xl-block > ul > li:nth-child(1) > span:nth-child(1)')

    load_circle_pop = (
        By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-auto.ml-auto.d-none.d-xl-block > ul > li:nth-child(1) > span.circle-pop')

    favourites_label = (
        By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-auto.ml-auto.d-none.d-xl-block > ul > li:nth-child(2) > span')

    account_label = (
        By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-auto.ml-auto.d-none.d-xl-block > ul > li:nth-child(3) > span')

    logout_label = (
        By.CSS_SELECTOR, 'product > header > header-options > div > div > div.col-auto.ml-auto.d-none.d-xl-block > ul > li:nth-child(4) > span')

    # home-page
    product_image = (
        By.CSS_SELECTOR, '#homeMainSlider > div > div > div > div > div.col-md-6.order-last.order-xl-last.order-lg-last.order-md-last.order-1 > img')

    exclusive_label = (
        By.CSS_SELECTOR, '#homeMainSlider > div > div > div > div > div.col-md-6.order-xl-first.order-lg-first.order-md-first.order-2 > div > div > h5')

    build_label = (
        By.CSS_SELECTOR, '#homeMainSlider > div > div > div > div > div.col-md-6.order-xl-first.order-lg-first.order-md-first.order-2 > div > div > p')

    view_all_products_btn = (
        By.CSS_SELECTOR, '#homeMainSlider > div > div > div > div > div.col-md-6.order-xl-first.order-lg-first.order-md-first.order-2 > div > div > a')

    loads_in_progress_view_all_label = (
        By.CSS_SELECTOR, 'product > ng-component > div:nth-child(2) > div > div > h2')

    view_products_by_category_label = (
        By.CSS_SELECTOR, 'product > ng-component > div:nth-child(4) > h2')

from selenium.webdriver.common.by import By


class HomePageLocators(object):

    search_bar = (By.CSS_SELECTOR, 'body > app-root > product > header > header-options >'
                                   ' div > div > div.col-xl-4.col-lg-5.col-md-5.col-12.search-box-m > form > input')
    categories_link = (By.ID, 'navDropDown-1')
    category_dropdpwn = (By.CSS_SELECTOR, 'div.show > div:nth-child(1) > div:nth-child(1) > div.row.product-list')
    total_categories = (By.CSS_SELECTOR, 'div.show > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    single_category = (By.CSS_SELECTOR, 'div.col-sm-4')
    category_name = (By.CSS_SELECTOR, 'h3:nth-child(2)')
    no_of_products_categories_list = (By.CSS_SELECTOR, 'div:nth-child(3)')
    cart = (By.CLASS_NAME, 'cart-outer')
    loader = (By.CLASS_NAME, 'centered')
    search = (By.NAME, 'search')
    search_button = (By.CSS_SELECTOR, '.search-box-header > button:nth-child(2)')


class AllProductsLocators(object):
    panel_title = (By.CLASS_NAME, 'panel-title')
    panel_no_of_products = (By.CLASS_NAME, 'm-0')
    breadcrumb = (By.CLASS_NAME, 'breadcrumb-page')
    breadcrumb_links_total = (By.TAG_NAME, 'a')
    page_menu = (By.CLASS_NAME, 'page-title-menu')
    all_menus = (By.TAG_NAME, 'li')
    sorting_by_price = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2)')
    sorting_by_warehouse = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2) > a:nth-child(1)')
    low_to_high = (By.ID, 'customCheck21')
    high_to_low = (By.ID, 'customCheck22')
    product_list = (By.CSS_SELECTOR, 'div.product-list:nth-child(4)')
    single_product = (By.CSS_SELECTOR, 'div.col-lg-4')
    cost = (By.CSS_SELECTOR, 'div:nth-child(3) > span:nth-child(1)')
    product_column = (By.CSS_SELECTOR, 'div.product-list:nth-child(4)')
    product_cell = (By.CSS_SELECTOR, 'div.col-lg-4')
    product_cell_price = (By.CSS_SELECTOR, 'div:nth-child(3) > span:nth-child(1)')
    sort_lower = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > label:nth-child(2)')
    sort_higher = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2) > div:nth-child(2) > form:nth-child(1) >'
                                    ' div:nth-child(2) > label:nth-child(2)')
    sort_apply_button = (By.CSS_SELECTOR, 'button.btn:nth-child(3)')
    loader = (By.CLASS_NAME, 'centered')
    no_products = (By.CLASS_NAME, 'load-not-avd')

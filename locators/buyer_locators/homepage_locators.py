from selenium.webdriver.common.by import By


class HomePageLocators(object):

    search_bar = (By.NAME, 'search')
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
    brands_link = (By.ID, 'navDropDown-2')
    brands_menu = (By.CSS_SELECTOR, 'div.mega-menu.show')
    brands_menu_list = (By.CSS_SELECTOR, 'div.col-sm-3.mb-4')
    brands_images = (By.CSS_SELECTOR, 'div:nth-child(1) > img:nth-child(1)')
    brand_name = (By.CSS_SELECTOR, 'h3:nth-child(2)')
    brand_numbers = (By.CSS_SELECTOR, 'div:nth-child(3)')


class ResultsPageLocators(object):
    products_rows = (By.CSS_SELECTOR, 'div.col-xl-3.mb-4')
    brands_category_page = (By.CSS_SELECTOR, 'div.col-md-12:nth-child(1)')


class AllProductsLocators(object):
    panel_title = (By.CLASS_NAME, 'panel-title')
    panel_no_of_products = (By.CLASS_NAME, 'm-0')
    breadcrumb = (By.CLASS_NAME, 'breadcrumb-page')
    breadcrumb_links_total = (By.TAG_NAME, 'a')
    page_menu = (By.CLASS_NAME, 'page-title-menu')
    all_menus = (By.TAG_NAME, 'li')
    sorting_by_price = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2)')
    sorting_by_warehouse = (By.CSS_SELECTOR, 'div.dropdown:nth-child(1) > a:nth-child(1)')
    low_to_high = (By.ID, 'customCheck21')
    high_to_low = (By.ID, 'customCheck22')
    product_list = (By.CSS_SELECTOR, 'div.product-list:nth-child(4)')
    single_product = (By.CSS_SELECTOR, 'div.col-lg-4')
    cost = (By.CSS_SELECTOR, 'div:nth-child(3) > span:nth-child(1)')
    product_column = (By.CSS_SELECTOR, 'div.product-list:nth-child(4)')
    product_cell = (By.CSS_SELECTOR, 'div.col-lg-4')
    product_cell_price = (By.CSS_SELECTOR, 'div:nth-child(3) > span:nth-child(1)')
    sort_lower = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1)'
                                   ' > label:nth-child(2)')
    sort_higher = (By.CSS_SELECTOR, 'div.dropdown:nth-child(2) > div:nth-child(2) > form:nth-child(1) >'
                                    ' div:nth-child(2) > label:nth-child(2)')
    sort_apply_button = (By.CSS_SELECTOR, 'button.btn:nth-child(3)')
    loader = (By.CLASS_NAME, 'centered')
    no_products = (By.CLASS_NAME, 'load-not-avd')
    de_select_warehouse = (By.CSS_SELECTOR, 'div.show:nth-child(2) > form:nth-child(1)')
    warehouse_apply_button = (By.CSS_SELECTOR, 'button.pt-2:nth-child(2)')
    warehouse_dropdown = (By.CSS_SELECTOR, 'div.dropdown:nth-child(1) > div:nth-child(2) > form:nth-child(1)')
    warehouse_drop_down_values = (By.CSS_SELECTOR, '.custom-control')


class ProductDetailsLocator(object):
    purchase_box = (By.CSS_SELECTOR, '.stock-available-box')
    product_quantity_dropdown = (By.CSS_SELECTOR, 'input[placeholder="Select Quantity"]')
    product_quantity = (By.CSS_SELECTOR, '.ng2-auto-complete-wrapper > ng2-auto-complete > div > ul')
    warehouse_locations_tabs = (By.ID, 'stock-available-tabs')
    warehouse_tab_link = (By.ID, 'Ronkonkoma')
    add_to_load = (By.CSS_SELECTOR, 'button.btn-green:nth-child(1)')
    truck_types = (By.CSS_SELECTOR, '#truckLoadmodal > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > '
                                    'div:nth-child(2)')
    truck = (By.CSS_SELECTOR, '.col-md-4.mb-3')
    confirmation_load = (By.CSS_SELECTOR, '#addToLoad > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > '
                                          'button:nth-child(2)')
    add_to_load_loader = (By.CSS_SELECTOR, '#stockAvailableTabContent > div.row > div:nth-child(2) > div > button > '
                                           'i[hidden]')
    added_products = (By.CLASS_NAME, 'load-scroll')
    product_single = (By.CSS_SELECTOR, 'div[_ngcontent-c4=""]')
    selected_product_name = (By.CSS_SELECTOR, '.col-xl-8 > h2:nth-child(1)')
    checkout_button = (By.CSS_SELECTOR, 'button.position-relative')
    load_percentage = (By.CSS_SELECTOR, '.text-md-right > h2:nth-child(2)')

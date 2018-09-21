from selenium.webdriver.common.by import By

class SupplierPageLocators(object):

    signin = (By.CLASS_NAME, 'btn-primary')
    kirv_logo = (By.XPATH, '//img[@alt = "KIRV"]')
    products_link = (By.XPATH, '//*[@id = "main-navigation"]/ul/li[1]/span')
    customers_link = (By.XPATH, '//*[@id = "main-navigation"]/ul/li[2]/span')
    input_search_customers = (By.XPATH, '//input[@placeholder="Search Customers"]')
    search_button = (By.XPATH, '//button[text() = "Search"]')
    logout_button = (By.XPATH, '//span[text() = "Logout"]')
    customers_title = (By.CLASS_NAME, 'page-title')
    all_customer_link = (By.XPATH, '//a[text()="All Customers"]')
    pending_link = (By.XPATH, '//a[text()="Pending"]')
    active_link = (By.XPATH, '//a[text()="Active"]')
    inactive_link = (By.XPATH, '//a[text()="Inactive"]')
    customer_name = (By.XPATH, '//th[text()="CUSTOMER NAME"]')
    state = (By.XPATH, '//th[text()="STATE"]')
    no_of_locations = (By.XPATH, '//th[text()="NO. OF LOCATION"]')
    main_contact = (By.XPATH, '//th[text()="MAIN CONTACT"]')
    phone_number = (By.XPATH, '//th[text()="PHONE NUMBER"]')
    account_status = (By.XPATH, '//th[text()="ACCOUNT STATUS"]')

from selenium.webdriver.common.by import By


class MainPage:
    SIGNIN = (By.CLASS_NAME, 'login')
    LOG = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SIGNIN_BUTTON = (By.ID, 'SubmitLogin')
    NAME_USER = (By.CLASS_NAME, 'header_user_info')

class ShopPage:
    SECTION_WOMEN = (By.XPATH, "//a[text()='Women']")

    SUBCATEG_TOPS = (By.CLASS_NAME, 'subcategory-image')
    COLOR_BLACK = (By.ID, 'layered_id_attribute_group_11')
    COLOR_BLACK_PRODUCT = (By.ID, 'color_7')
    ENABLED_FILTERS = (By.ID, 'enabled_filters')
    CHOOSSING_COLOR_BLACK = (By.XPATH, "//div[@id='enabled_filters']//li")

    VIEW_PRODUCT_TOPS = (By.CLASS_NAME, 'first-item-of-tablet-line')
    BUTTON_QUICK_VIEW_BLOUSE = (By.CLASS_NAME, 'quick-view')
    #FRAME = (By.CSS_SELECTOR, "#fancybox-frame")
    FRAME = (By.CSS_SELECTOR, ".fancybox-inner > iframe")

    CHOOSING_SIZE_BLOUSE = (By.ID, 'uniform-group_1')
    SIZE_M_BLOUSE = ((By.XPATH, "//option[@title='M']"))

    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".exclusive")
    WINDOW_WITH_ADDED_ITEMS = (By.CSS_SELECTOR, "#layer_cart")
    TEXT_ABOUT_SUCCESSFUL_ADDING = ((By.XPATH, "//h2"))
    ATTRIBUTES_OF_ITEMS = (By.ID, 'layer_cart_product_attributes')
    BUTTON_CONTINUE_SHOPPING = (By.CLASS_NAME, 'exclusive-medium')

    CATEG_DRESSES = (By.XPATH, "//div/a[@title='Dresses']")
    SUBCATEG_SUMMER_DRESSES = (By.XPATH, "//div/a[@title='Summer Dresses']")
    CHECKBOX_OF_MIDI_DRESS = (By.ID, 'uniform-layered_id_feature_20')
    VIEW_PRODUCT_DRESS = ((By.CLASS_NAME, 'first-item-of-tablet-line'))
    CHOOSING_SIZE_DRESS = (By.ID, 'group_1')
    SIZE_M_DRESS = ((By.XPATH, "//option[@title='M']"))
    COLOR_DRESS = (By.ID, 'color_15')

    NUMBER_ITEMS_IN_CART = (By.XPATH, '//a/span[@class="ajax_cart_quantity"]')
    CART = (By.XPATH, '//div/a[@title="View my shopping cart"]')

class Cart:
    BLOUSE = (By.XPATH, '//p/a[text() = "Blouse"]')
    PRINTED_CHIFFON_DRESS = (By.XPATH, '//td/p/a[text()="Printed Chiffon Dress"]')
    INCREASE_QUANTITY_OF_DRESSES = (By.ID, 'cart_quantity_up_7_38_0_733041')
    ACTUAL_QUANTITY = (By.XPATH, '//input[@value="2"]')
    BUTTON_PROCEED_TO_CHECKOUT = (By.XPATH, '//a[@class = "button btn btn-default standard-checkout button-medium"]')
    BUTTON_PROCEED_TO_CHECKOUT_ADDRESS = (By.XPATH, '//button[@class = "button btn btn-default button-medium"]')
    AGREEMENT_WITH_TERMS = (By.XPATH, '//input[@id = "cgv"]')
    PAYMENT_BY_BANK_WIRE = (By.XPATH, '//a[@class = "bankwire"]')
    BUTTON_CONFIRM_ORDER = (By.XPATH, '//span[text()="I confirm my order"]')
    INFO_ABOUT_ORDER = (By.CLASS_NAME, 'cheque-indent')
    BUTTON_BACK_TO_ORDERS = (By.XPATH, '//a[@class = "button-exclusive btn btn-default"]')
    STATUS_OF_ORDER = (By.XPATH, '//tr[@class="first_item "]/td[@class="history_state"]')
    BUTTON_HOME = (By.XPATH, '//li/a[@class="btn btn-default button button-small"]/span[text()=" Home"]')
    BUTTON_PROCEED_TO_CHECKOUT_SHIPPING = (By.XPATH, '//button[@class = "button btn btn-default standard-checkout button-medium"]')











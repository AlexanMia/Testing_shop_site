from selenium.webdriver.common.by import By


class MainPage:
    SIGNIN = (By.CLASS_NAME, 'login')
    LOG = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    SIGNIN_BUTTON = (By.ID, 'SubmitLogin')
    NAME_USER = (By.CLASS_NAME, 'header_user_info')

class ShopPage:
    SECTION_WOMEN = (By.XPATH, "//a[text()='Women']")

    CATEG_TOPS = (By.CLASS_NAME, 'subcategory-image')
    COLOR_BLACK = (By.ID, 'layered_id_attribute_group_11')
    COLOR_BLACK_PRODUCT = (By.ID, 'color_7')

    CHOOSSING_FILTERS_LOGS = (By.XPATH, "//div[@id='enabled_filters']//li")

    VIEW_PRODUCT_TOPS = (By.CLASS_NAME, 'first-item-of-tablet-line')
    BUTTON_QUICK_VIEW_BLOUSE = (By.CLASS_NAME, 'quick-view')
    FRAME = (By.CSS_SELECTOR, ".fancybox-inner > iframe")

    CHOOSING_SIZE_BLOUSE = (By.ID, 'uniform-group_1')
    SIZE_M_ARTICLE = (By.XPATH, "//option[@title='M']")

    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".exclusive")
    WINDOW_WITH_ADDED_ITEMS = (By.CSS_SELECTOR, "#layer_cart")
    TEXT_ABOUT_SUCCESSFUL_ADDING = (By.XPATH, "//div[@class='layer_cart_product col-xs-12 col-md-6']/h2")

    ATTRIBUTES_OF_ITEMS = (By.ID, 'layer_cart_product_attributes')
    BUTTON_CONTINUE_SHOPPING = (By.CLASS_NAME, 'exclusive-medium')

    CATEG_DRESSES = (By.XPATH, "//div/a[@title='Dresses']")
    SUBCATEG_SUMMER_DRESSES = (By.XPATH, "//div/a[@title='Summer Dresses']")
    CHECKBOX_OF_MIDI_DRESS = (By.ID, 'uniform-layered_id_feature_20')
    CHECKBOX_OF_MIDI_DRESS_2 = (By.XPATH, "//span[@class]/input[@type='checkbox' and @class='checkbox']")
    VIEW_PRODUCT_DRESS = (By.CLASS_NAME, 'first-item-of-tablet-line')
    CHOOSING_SIZE_DRESS = (By.ID, 'group_1')

    COLOR_DRESS = (By.ID, 'color_15')

    NUMBER_ITEMS_IN_CART = (By.XPATH, '//a/span[@class="ajax_cart_quantity"]')
    CART = (By.XPATH, '//div/a[@title="View my shopping cart"]')

    SECTION_T_SHIRTS = (By.XPATH, '//ul[@class]/li[3]/a[@title="T-shirts"]')
    ITEM_T_SHIRT = (By.XPATH, '//li[@class]/div[@class="product-container"]')
    BUTTON_ADD_TO_WISHLIST = (By.XPATH, '//div[@class="wishlist"]')
    WINDOW_AND_NOTE_ADD_TO_WISHLIST = (By.XPATH, '//div[@class="fancybox-outer"]//p')
    BUTTON_CLOSE_WINDOW_NOTE_ADD_TO_WISHLIST = (By.XPATH, '//div[@class="fancybox-wrap fancybox-desktop fancybox-type-html fancybox-opened"]//a')
    NAME_T_SHIRT = (By.XPATH, '//h5[@itemprop="name"]/a[@class="product-name"]')

    SECTION_DRESSES = (By.XPATH, '//div/ul[@class]/li[2]/a[@title="Dresses"]')
    ITEM_DRESS = (By.XPATH, '//ul/li[@class = "ajax_block_product col-xs-12 col-sm-6 col-md-4 last-in-line first-item-of-tablet-line last-item-of-mobile-line"]/div[@class="product-container"]')
    BUTTON_ADD_TO_WISHLIST_DRESS = (By.XPATH, '//div[@class="wishlist"]//a[@class="addToWishlist wishlistProd_5"]')
    NAME_DRESS = (By.XPATH, '//li[@class="ajax_block_product col-xs-12 col-sm-6 col-md-4 last-in-line first-item-of-tablet-line last-item-of-mobile-line"]//h5[@itemprop="name"]/a[@class="product-name"]')

    SECTION_EVENING_DRESSES = (By.XPATH, '//div[@id="subcategories"]//li//a[@title="Evening Dresses"]')
    ITEM_EVENING_DRESS = (By.XPATH, '//li[@class="ajax_block_product col-xs-12 col-sm-6 col-md-4 first-in-line last-line first-item-of-tablet-line first-item-of-mobile-line last-mobile-line"]')
    NAME_EVENING_DRESS = (By.XPATH, '//h5[@itemprop="name"]/a[@class="product-name"]')
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


class Wishlist:
    ACCOUNT = (By.XPATH, '//div[@class]/a[@class="account"]')
    BUTTON_WISHLIST = (By.XPATH, '//li[@class="lnk_wishlist"]')
    WISHLIST_TABLE = (By.XPATH, '//tr[@id]')
    QUANTITY_OF_ITEMS = (By.XPATH, '//tr[@id]/td[@class="bold align_center"]')
    NOTE_MY_WISHLIST = (By.XPATH, '//td[@style]/a[@href]')
    PLACE_WITH_ALL_ITEMS_IN_WISHLIST = (By.XPATH, '//div[@class="wishlistLinkTop"]')

    LOCATORS_ITEMS_IN_WISHLIST = [(By.XPATH, '//li[@id="wlp_1_0"]//p[@id]'),
                                  (By.XPATH, '//li[@id="wlp_4_0"]//p[@id]'),
                                  (By.XPATH, '//li[@id="wlp_5_0"]//p[@id]')]

    OPTION_QUANTITY_OF_ITEMS = (By.XPATH, '//p[@class="form-group"]/input[@id="quantity_1_0"]')
    BUTTON_SAVE_OF_FIRST_ITEM = (By.XPATH, '//li[@id="wlp_1_0"]//div[@class="btn_action"]/a[@class="btn btn-default button button-small"]')

    OPTION_PRIORITY_OF_ITEM = (By.XPATH, '//p[@class="form-group"]/select[@id="priority_4_0"]/option[@value="0"]')
    BUTTON_SAVE_OF_SECOND_ITEM = (By.XPATH, '//li[@id="wlp_4_0"]//div[@class="btn_action"]/a[@class="btn btn-default button button-small"]')

    BUTTON_DELETE_OF_THIRD_ITEM = (By.XPATH, '//li[@id="wlp_5_0"]//a[@class="lnkdel"]')

    QUANTITY_OF_FIRST_ITEM = (By.XPATH, '//p[@class="form-group"]/input[@value="3"]')
    PRIORITY_OF_SECOND_ITEM = (By.XPATH, '//p[@class="form-group"]/select[@id="priority_4_0"]/option[@selected="selected" and @value="0"]')
    THIRD_ITEM = (By.ID, 'wlp_5_19')

    BUTTON_DELETE_WISHLIST = (By.XPATH, '//td[@class="wishlist_delete"]/a')

    TABLE_WISHLIST = (By.ID, 'block-history')

    BUTTON_HOME = (By.XPATH, '//li[2]/a[@class="btn btn-default button button-small"]')

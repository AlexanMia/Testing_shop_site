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

    VIEW_PRODUCT = (By.CLASS_NAME, 'first-item-of-tablet-line')
    BUTTON_QUICK_VIEW_BLOUSE = (By.CLASS_NAME, 'quick-view')
    #FRAME = (By.CSS_SELECTOR, "#fancybox-frame")
    FRAME = (By.CSS_SELECTOR, ".fancybox-inner > iframe")

    CHOOSING_SIZE = (By.ID, 'uniform-group_1')
    SIZE_M = ((By.XPATH, "//option[@title='M']"))










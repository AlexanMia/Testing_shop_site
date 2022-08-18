import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_base import TestBase
from util.constants import Constants
from util.locators import ShopPage, Cart

from selenium.webdriver.support import expected_conditions as EC


class TestEndToEnd(TestBase):
    def test_open_site(self, browser):
        global page
        page = super().init_page(browser)
        super().open_page()

    def test_successful_login(self):
        super().get_to_log_in()
        super().check_proper_user()


    # параметризовать??
    # choose some dresses
    def test_add_to_basket(self, browser):
        # go to WOMEN section
        global page
        page.element_click(ShopPage.SECTION_WOMEN)
        # go to Subcategories TOPS
        page.element_click(ShopPage.SUBCATEG_TOPS)
        # choose color of blouse
        page.element_click(ShopPage.COLOR_BLACK)
        # time.sleep(10)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(ShopPage.CHOOSSING_COLOR_BLACK))
        assert Constants.CHECKING_COLOR_BLACK.capitalize() in page.get_elements_text(ShopPage.CHOOSSING_COLOR_BLACK), \
            f'{Constants.CHECKING_COLOR_BLACK } is not chosen'

        assert Constants.CHECKING_COLOR_BLACK in page.find_need_element(ShopPage.COLOR_BLACK_PRODUCT).get_attribute('href'), \
        f'Choosing Color is not {Constants.CHECKING_COLOR_BLACK}'

        # ФРЕЙМ товара
        # Поместите элементы, над которыми нужно навести курсор
        hover_element = page.find_need_element(ShopPage.VIEW_PRODUCT_TOPS)
        hidden_bitton = page.find_need_element(ShopPage.BUTTON_QUICK_VIEW_BLOUSE)
        # Выполните операцию наведения на элемент
        actions = ActionChains(browser)
        actions.move_to_element(hover_element)
        actions.click(hidden_bitton)
        actions.perform()
        #time.sleep(10)
        assert page.find_need_element(ShopPage.FRAME), 'Iframe is not be found'
        page.switch_to_product_page(browser, ShopPage.FRAME)
        # выбрать размер
        page.element_click(ShopPage.CHOOSING_SIZE_BLOUSE)
        page.element_click(ShopPage.SIZE_M_BLOUSE)
        # добавить в корзину
        page.element_click(ShopPage.BUTTON_ADD_TO_CART)
        #time.sleep(10)
        browser.switch_to.default_content()
        time.sleep(10)
        # появилось окно с айди layer_cart
        assert page.find_need_element(ShopPage.WINDOW_WITH_ADDED_ITEMS), 'Window with added items is not be found'
        # подтверждение добавления в корзину надпись Product successfully added to your shopping cart h2 с текстом successfully added
        assert 'successfully added' in page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING), \
            f'Expected text successfully added is not in {page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)}'
        # нужный цвет и нужный размер id = layer_cart_product_attributes текст Black, M
        assert 'Black, M' in page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS), \
            f'Black, M != {page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)}'
        # нажать кнопку Continue shopping class = continue btn btn-default button exclusive-medium
        page.element_click(ShopPage.BUTTON_CONTINUE_SHOPPING)
        time.sleep(10)


        # добавить еще 2-3 товара с использованием разных фильтров
        # перейти в раздел Women
        page.element_click(ShopPage.SECTION_WOMEN)
        # перейти в раздел  платья
        page.element_click(ShopPage.CATEG_DRESSES)
        # перейти в подраздел летние платья
        page.element_click(ShopPage.SUBCATEG_SUMMER_DRESSES)
        # выбрать чекбокс с миди платьями
        page.element_click(ShopPage.CHECKBOX_OF_MIDI_DRESS)
        time.sleep(10)

        # ФРЕЙМ товара
        # Поместите элементы, над которыми нужно навести курсор
        hover_element = page.find_need_element(ShopPage.VIEW_PRODUCT_DRESS)
        hidden_bitton = page.find_need_element(ShopPage.BUTTON_QUICK_VIEW_BLOUSE)
        # Выполните операцию наведения на элемент
        actions = ActionChains(browser)
        actions.move_to_element(hover_element)
        actions.click(hidden_bitton)
        actions.perform()
        # time.sleep(10)
        assert page.find_need_element(ShopPage.FRAME), 'Iframe is not be found'
        page.switch_to_product_page(browser, ShopPage.FRAME)
        # выбрать размер и цвет
        page.element_click(ShopPage.CHOOSING_SIZE_DRESS)
        page.element_click(ShopPage.SIZE_M_DRESS)
        page.element_click(ShopPage.COLOR_DRESS)
        # добавить в корзину
        page.element_click(ShopPage.BUTTON_ADD_TO_CART)
        # time.sleep(10)
        browser.switch_to.default_content()
        time.sleep(10)
        # появилось окно с айди layer_cart
        assert page.find_need_element(ShopPage.WINDOW_WITH_ADDED_ITEMS), 'Window with added items is not be found'
        # подтверждение добавления в корзину надпись Product successfully added to your shopping cart h2
        # с текстом successfully added
        assert 'successfully added' in page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING), \
        f'Expected text successfully added is not in {page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)}'
        # нужный цвет и нужный размер id = layer_cart_product_attributes текст Black, M
        assert 'Green, M' in page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS), \
        f'Green, M != {page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)}'
        # нажать кнопку Continue shopping class = continue btn btn-default button exclusive-medium
        page.element_click(ShopPage.BUTTON_CONTINUE_SHOPPING)
        time.sleep(10)
        browser.switch_to.default_content()

    def test_making_an_order(self):

        # проверить что в корзине действительно два товара
        assert "2" == page.get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART), f'the number of products does not match -> ' \
                                                                             f'{page.get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART)} != "2"'
        # div class shopping_cart -> span class ajax_cart_quantity
        # перейти в корзину а title View my shopping cart
        page.element_click(ShopPage.CART)

        # проверить что в корзине лежат нужные товары tr class cart_item last_item address_733041 even, a text Printed Chiffon Dress
        # tr class cart_item first_item address_733041 odd, a text Blouse
        assert page.find_need_element(Cart.BLOUSE) and page.find_need_element(Cart.PRINTED_CHIFFON_DRESS)
        # увеличить количество платьев до 2 id cart_quantity_up_7_38_0_733041
        page.element_click(Cart.INCREASE_QUANTITY_OF_DRESSES)
        assert '2' == page.find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value"), \
            f'the number of dresses does not match -> {page.find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value")} != "2"'
        # нажать кнопку Proceed to checkout a class standard-checkout
        page.element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT)

        # снова нажать кнопку //button[@class = 'button btn btn-default button-medium']
        page.element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT_ADDRESS)
        # agree with terms //input[@id = 'cgv']
        page.element_click(Cart.AGREEMENT_WITH_TERMS)

        # нажать кнопку Proceed to checkout a class standard-checkout
        page.element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT_SHIPPING)
        # choose kind of payment //a[@class = 'bankwire'] CLICK
        page.element_click(Cart.PAYMENT_BY_BANK_WIRE)

        # confirm your order //span[text()='I confirm my order'] CLICK
        page.element_click(Cart.BUTTON_CONFIRM_ORDER)
        # check information about order class cheque-indent взять оттуда текст и проверить вхождение туда слов Your order on My Store is complete.
        assert Constants.INFO_ABOUT_ORDER == page.get_elements_text(Cart.INFO_ABOUT_ORDER), \
            f'Expected text {Constants.INFO_ABOUT_ORDER} is not equal {page.get_elements_text(Cart.INFO_ABOUT_ORDER)}'
        # посмотреть свои заказы нажать на кнопку Back to orders: a class button-exclusive
        page.element_click(Cart.BUTTON_BACK_TO_ORDERS)
        # найти столбец с предварительным заказом class history_state с текстом On backorder
        assert Constants.STATUS_ORDER_TEXT == page.get_elements_text(Cart.STATUS_OF_ORDER), \
            f'Expected status {Constants.STATUS_ORDER_TEXT} is not equal actual status {page.get_elements_text(Cart.STATUS_OF_ORDER)}'
        # нажать на кпнку домой //li/a[@class='btn btn-default button button-small']/span[text()=' Home']
        page.element_click(Cart.BUTTON_HOME)













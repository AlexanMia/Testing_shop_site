import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_base import TestBase
from util.constants import Constants
from util.locators import ShopPage, Cart

from selenium.webdriver.support import expected_conditions as EC


class TestEndToEnd(TestBase):

    @pytest.fixture(scope='class', autouse=True)
    def open_site(self, browser):
        global page
        page = super().init_page(browser)
        super().open_page()

    def test_successful_login(self):
        super().get_to_log_in()
        # вынести метод сюда, если он нигде больше не будет использоваться
        super().check_proper_user()



    @pytest.mark.parametrize('loc_section_women,'
                             'loc_subcateg_tops,'
                             'loc_colour_black,'
                             'const_color_black,'
                             'loc_choosing_color_logs,'
                             'color_black_product,'
                             'frame_article_loc_hover,'
                             'frame_article_loc_hidden,'
                             'frame,'
                             'list_of_size,'
                             'size_M,'
                             'button_add_to_cart,'
                             'window_with_added_items,'
                             'text_about_succeessful_adding,'
                             'expected_col_and_size,'
                             'actual_col_and_size,'
                             'button_continue_shopping', [
        (ShopPage.SECTION_WOMEN,
         ShopPage.CATEG_TOPS,
         ShopPage.COLOR_BLACK,
         Constants.CHECKING_COLOR_BLACK,
         ShopPage.CHOOSSING_FILTERS_LOGS,
         ShopPage.COLOR_BLACK_PRODUCT,
         ShopPage.VIEW_PRODUCT_TOPS,
         ShopPage.BUTTON_QUICK_VIEW_BLOUSE,
         ShopPage.FRAME,
         ShopPage.CHOOSING_SIZE_BLOUSE,
         ShopPage.SIZE_M_ARTICLE,
         ShopPage.BUTTON_ADD_TO_CART,
         ShopPage.WINDOW_WITH_ADDED_ITEMS,
         ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING,
         Constants.EXPECTED_COLORS_AND_SIZE_OF_BLOUSE,
         ShopPage.ATTRIBUTES_OF_ITEMS,
         ShopPage.BUTTON_CONTINUE_SHOPPING)
    ])
    # параметризовать??
    # choose some dresses
    def test_add_to_cart(self, browser, loc_section_women,
                         loc_subcateg_tops,
                         loc_colour_black,
                         const_color_black,
                         loc_choosing_color_logs,
                         color_black_product,
                         frame_article_loc_hover,
                         frame_article_loc_hidden,
                         frame,
                         list_of_size,
                         size_M,
                         button_add_to_cart,
                         window_with_added_items,
                         text_about_succeessful_adding,
                         expected_col_and_size,
                         actual_col_and_size,
                         button_continue_shopping):

        global page
        page.element_click(loc_section_women)

        page.element_click(loc_subcateg_tops)

        page.element_click(loc_colour_black)

        # time.sleep(10)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located(ShopPage.CHOOSSING_COLOR_BLACK))

        assert const_color_black.capitalize() in page.get_elements_text(loc_choosing_color_logs), \
            f'{Constants.CHECKING_COLOR_BLACK} is not chosen'

        assert const_color_black in page.find_need_element(color_black_product).get_attribute('href'), \
        f'Choosing Color is not {Constants.CHECKING_COLOR_BLACK}'

        # ФРЕЙМ товара
        super().hover_to_click_hidden_button(browser, frame_article_loc_hover, frame_article_loc_hidden)

        assert page.find_need_element(frame), 'Iframe is not be found'
        page.switch_to_frame(browser, frame)

        page.element_click(list_of_size)
        page.element_click(size_M)

        page.element_click(button_add_to_cart)
        #time.sleep(10)
        page.switch_to_default_content(browser)
        time.sleep(10)

        assert page.find_need_element(window_with_added_items), 'Window with added items is not be found'

        assert Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS in page.get_elements_text(text_about_succeessful_adding), \
            f'Expected text {Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS} is not in {page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)}'

        assert Constants.EXPECTED_COLORS_AND_SIZE_OF_BLOUSE in page.get_elements_text(actual_col_and_size), \
            f'Black, M != {page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)}'

        page.element_click(button_continue_shopping)
        time.sleep(10)



        # new section
        page.element_click(ShopPage.SECTION_WOMEN)

        page.element_click(ShopPage.CATEG_DRESSES)
        # TODO ОТЛИЧИЕ!!!!!
        #page.element_click(ShopPage.SUBCATEG_SUMMER_DRESSES)

        page.element_click(ShopPage.CHECKBOX_OF_MIDI_DRESS)
        time.sleep(10)
        # //span[@class]/input[@type='checkbox' and @class='checkbox' ]
        assert page.is_element_selected(ShopPage.CHECKBOX_OF_MIDI_DRESS_2), 'Length is not choosen'
        assert Constants.CHECKING_MIDI_DRESS in page.get_elements_text(ShopPage.CHOOSSING_FILTERS_LOGS), \
            f'{Constants.CHECKING_MIDI_DRESS} is not chosen'





        # ФРЕЙМ товара
        super().hover_to_click_hidden_button(browser, ShopPage.VIEW_PRODUCT_DRESS, ShopPage.BUTTON_QUICK_VIEW_BLOUSE)

        assert page.find_need_element(ShopPage.FRAME), 'Iframe is not be found'
        page.switch_to_frame(browser, ShopPage.FRAME)

        page.element_click(ShopPage.CHOOSING_SIZE_DRESS)
        page.element_click(ShopPage.SIZE_M_ARTICLE)
        page.element_click(ShopPage.COLOR_DRESS)

        page.element_click(ShopPage.BUTTON_ADD_TO_CART)
        # time.sleep(10)
        page.switch_to_default_content(browser)
        time.sleep(10)

        assert page.find_need_element(ShopPage.WINDOW_WITH_ADDED_ITEMS), 'Window with added items is not be found'


        assert Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS in page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING), \
        f'Expected text {Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS} is not in {page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)}'

        assert Constants.EXPECTED_COLORS_AND_SIZE_OF_DRESS in page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS), \
        f'{Constants.EXPECTED_COLORS_AND_SIZE_OF_DRESS} != {page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)}'

        page.element_click(ShopPage.BUTTON_CONTINUE_SHOPPING)
        time.sleep(10)
        #browser.switch_to.default_content()

    def test_making_an_order(self):
        assert Constants.NUMBER_OF_ITEMS_IN_CART  == page.get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART), \
            f'the number of products does not match -> {page.get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART)} != {Constants.NUMBER_OF_ITEMS_IN_CART}'

        page.element_click(ShopPage.CART)

        assert page.find_need_element(Cart.BLOUSE) and page.find_need_element(Cart.PRINTED_CHIFFON_DRESS)

        page.element_click(Cart.INCREASE_QUANTITY_OF_DRESSES)
        assert Constants.NUMBER_OF_DRESSES_IN_CART == page.find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value"), \
            f'the number of dresses does not match -> {page.find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value")} != {Constants.NUMBER_OF_DRESSES_IN_CART}'

        page.element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT)


        page.element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT_ADDRESS)

        page.element_click(Cart.AGREEMENT_WITH_TERMS)


        page.element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT_SHIPPING)

        page.element_click(Cart.PAYMENT_BY_BANK_WIRE)


        page.element_click(Cart.BUTTON_CONFIRM_ORDER)

        assert Constants.INFO_ABOUT_ORDER == page.get_elements_text(Cart.INFO_ABOUT_ORDER), \
            f'Expected text {Constants.INFO_ABOUT_ORDER} is not equal {page.get_elements_text(Cart.INFO_ABOUT_ORDER)}'

        page.element_click(Cart.BUTTON_BACK_TO_ORDERS)

        assert Constants.STATUS_ORDER_TEXT == page.get_elements_text(Cart.STATUS_OF_ORDER), \
            f'Expected status {Constants.STATUS_ORDER_TEXT} is not equal actual status {page.get_elements_text(Cart.STATUS_OF_ORDER)}'

        page.element_click(Cart.BUTTON_HOME)













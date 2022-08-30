import pytest
from test_base import TestBase
from util.constants import Constants
from util.locators import ShopPage, Cart


class TestEndToEnd(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global page
        page = super().get_page()

    def test_successful_login(self):
        super().log_in()
        super().check_proper_user()

    def test_add_to_cart_blouse_with_definite_filter_color(self):
        page.element_click(ShopPage.SECTION_WOMEN)
        page.element_click(ShopPage.CATEG_TOPS)
        page.element_click(ShopPage.COLOR_BLACK)

        assert Constants.CHECKING_COLOR_BLACK.capitalize() in page.get_elements_text(ShopPage.CHOOSSING_FILTERS_LOGS), \
            f'{Constants.CHECKING_COLOR_BLACK} is not chosen'

        assert Constants.CHECKING_COLOR_BLACK in page.find_need_element(ShopPage.COLOR_BLACK_PRODUCT).get_attribute('href'), \
        f'Choosing Color is not {Constants.CHECKING_COLOR_BLACK}'

        # Frame
        super().hover_to_click_hidden_button(ShopPage.VIEW_PRODUCT_TOPS, ShopPage.BUTTON_QUICK_VIEW_BLOUSE)

        assert page.find_need_element(ShopPage.FRAME), 'Iframe is not be found'

        page.switch_to_frame(ShopPage.FRAME)

        page.element_click(ShopPage.CHOOSING_SIZE_BLOUSE)
        page.element_click(ShopPage.SIZE_M_ARTICLE)
        page.element_click(ShopPage.BUTTON_ADD_TO_CART)

        page.switch_to_default_content()

        assert page.find_need_element(ShopPage.WINDOW_WITH_ADDED_ITEMS), 'Window with added items is not be found'
        super().wait_visibility_element(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)
        assert Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS in page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING), \
            f'Expected text {Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS} is not in {page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)}'
        assert Constants.EXPECTED_COLORS_AND_SIZE_OF_BLOUSE in page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS), \
            f'{Constants.EXPECTED_COLORS_AND_SIZE_OF_BLOUSE} != {page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)}'

        page.element_click(ShopPage.BUTTON_CONTINUE_SHOPPING)

    def test_add_to_cart_dress_with_definite_filter_length(self):
        page.element_click(ShopPage.SECTION_WOMEN)
        page.element_click(ShopPage.CATEG_DRESSES)
        page.element_click(ShopPage.SUBCATEG_SUMMER_DRESSES)
        page.element_click(ShopPage.CHECKBOX_OF_MIDI_DRESS)

        assert page.is_element_selected(ShopPage.CHECKBOX_OF_MIDI_DRESS_2), 'Length is not choosen'
        assert Constants.CHECKING_MIDI_DRESS in page.get_elements_text(ShopPage.CHOOSSING_FILTERS_LOGS), \
            f'{Constants.CHECKING_MIDI_DRESS} is not chosen'

        # Frame
        super().hover_to_click_hidden_button(ShopPage.VIEW_PRODUCT_DRESS, ShopPage.BUTTON_QUICK_VIEW_BLOUSE)

        assert page.find_need_element(ShopPage.FRAME), 'Iframe is not be found'
        page.switch_to_frame(ShopPage.FRAME)

        page.element_click(ShopPage.CHOOSING_SIZE_DRESS)
        page.element_click(ShopPage.SIZE_M_ARTICLE)
        page.element_click(ShopPage.COLOR_DRESS)
        page.element_click(ShopPage.BUTTON_ADD_TO_CART)

        page.switch_to_default_content()

        assert page.find_need_element(ShopPage.WINDOW_WITH_ADDED_ITEMS), 'Window with added items is not be found'
        super().wait_visibility_element(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)
        assert Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS in page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING), \
        f'Expected text {Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS} is not in {page.get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)}'
        assert Constants.EXPECTED_COLORS_AND_SIZE_OF_DRESS in page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS), \
        f'{Constants.EXPECTED_COLORS_AND_SIZE_OF_DRESS} != {page.get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)}'

        page.element_click(ShopPage.BUTTON_CONTINUE_SHOPPING)

    def test_making_an_order(self):
        assert Constants.NUMBER_OF_ITEMS_IN_CART == page.get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART), \
            f'the number of products does not match -> ' \
            f'{page.get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART)} != {Constants.NUMBER_OF_ITEMS_IN_CART}'

        page.element_click(ShopPage.CART)

        assert page.find_need_element(Cart.BLOUSE) and page.find_need_element(Cart.PRINTED_CHIFFON_DRESS)

        page.element_click(Cart.INCREASE_QUANTITY_OF_DRESSES)

        assert Constants.NUMBER_OF_DRESSES_IN_CART == page.find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value"), \
            f'the number of dresses does not match -> ' \
            f'{page.find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value")} != {Constants.NUMBER_OF_DRESSES_IN_CART}'

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

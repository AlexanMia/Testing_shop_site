import pytest
from test_base import TestBase
from util.constants import Constants


class TestEndToEnd(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global main_page
        global quick_view_page
        global cart_page
        main_page = super().get_main_page()
        quick_view_page = super().get_quick_view_page()
        cart_page = super().get_cart_page()

    def test_successful_login(self):
        super().log_in()
        super().check_proper_user()

    def test_add_to_cart_blouse_with_definite_filter_color(self):
        main_page.choose_black_tops_filter()
        assert Constants.CHECKING_COLOR_BLACK.capitalize() in main_page.get_choosing_filters_log(), \
            f'{Constants.CHECKING_COLOR_BLACK} is not chosen'
        assert Constants.CHECKING_COLOR_BLACK in main_page.get_black_color_attribute(), \
            f'Choosing Color is not {Constants.CHECKING_COLOR_BLACK}'
        # Frame
        main_page.click_blouse_quick_view()
        assert quick_view_page.find_frame(), 'Iframe is not be found'
        quick_view_page.switch_to_item_quick_view()
        quick_view_page.choose_m_size_blouse()
        quick_view_page.add_to_cart()
        main_page.switch_to_default_content()
        assert quick_view_page.find_window_with_added_items(), 'Window with added items is not be found'
        quick_view_page.wait_item_will_be_added_to_cart()
        assert Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS in quick_view_page.get_text_about_successful_adding(), \
            f'Expected text {Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS} is not in {quick_view_page.get_text_about_successful_adding()}'
        assert Constants.EXPECTED_COLORS_AND_SIZE_OF_BLOUSE in quick_view_page.get_item_attribute_text(), \
            f'{Constants.EXPECTED_COLORS_AND_SIZE_OF_BLOUSE} != {quick_view_page.get_item_attribute_text()}'
        quick_view_page.click_continue_shopping_button()

    def test_add_to_cart_dress_with_definite_filter_length(self):
        main_page.choose_midi_dress_filter()
        assert main_page.is_midi_dress_selected(), 'Length is not choosen'
        assert Constants.CHECKING_MIDI_DRESS in main_page.get_filter_log(), \
            f'{Constants.CHECKING_MIDI_DRESS} is not chosen'
        # Frame
        main_page.click_blouse_quick_view_in_dress()
        assert quick_view_page.find_frame(), 'Iframe is not be found'
        quick_view_page.switch_to_item_quick_view()
        quick_view_page.choose_m_size_dress()
        quick_view_page.add_to_cart()
        main_page.switch_to_default_content()
        assert quick_view_page.find_window_with_added_items(), 'Window with added items is not be found'
        quick_view_page.wait_item_will_be_added_to_cart()
        assert Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS in quick_view_page.get_text_about_successful_adding(), \
            f'Expected text {Constants.EXPECTED_TEXT_ABOUT_ADDING_ITEMS} is not in {quick_view_page.get_text_about_successful_adding()}'
        assert Constants.EXPECTED_COLORS_AND_SIZE_OF_DRESS in quick_view_page.get_item_attribute_text(), \
            f'{Constants.EXPECTED_COLORS_AND_SIZE_OF_DRESS} != {quick_view_page.get_item_attribute_text()}'
        quick_view_page.click_continue_shopping_button()

    def test_making_an_order(self):
        assert Constants.NUMBER_OF_ITEMS_IN_CART == main_page.get_cart_items_count(), \
            f'the number of products does not match -> ' \
            f'{main_page.get_cart_items_count()} != {Constants.NUMBER_OF_ITEMS_IN_CART}'
        main_page.go_to_cart()
        assert cart_page.are_items_in_the_cart(), 'There are not all need items'
        cart_page.increase_quantity_of_dresses()
        assert Constants.NUMBER_OF_DRESSES_IN_CART == cart_page.get_actual_items_count_in_the_cart(), \
            f'the number of dresses does not match -> ' \
            f'{cart_page.get_actual_items_count_in_the_cart()} != {Constants.NUMBER_OF_DRESSES_IN_CART}'
        cart_page.make_an_order()
        assert Constants.INFO_ABOUT_ORDER == cart_page.get_order_info(), f'Expected text {Constants.INFO_ABOUT_ORDER} ' \
                                                                         f'is not equal {cart_page.get_order_info()}'
        cart_page.go_to_order()
        assert Constants.STATUS_ORDER_TEXT == cart_page.get_order_status(), \
            f'Expected status {Constants.STATUS_ORDER_TEXT} is not equal actual status {cart_page.get_order_status()}'
        cart_page.click_home_button()

import pytest
from test_base import TestBase
from util.constants import Constants
from util.locators import ShopPage, Wishlist


class TestModuleWishlist(TestBase):
    expected_wishlist_items = []

    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global page
        page = super().get_page()

    def test_successful_login(self):
        super().log_in()
        super().check_proper_user()

    testdata = [
        (ShopPage.SECTION_T_SHIRTS, ShopPage.ITEM_T_SHIRT, ShopPage.BUTTON_ADD_TO_WISHLIST, ShopPage.NAME_T_SHIRT),
        (ShopPage.SECTION_DRESSES, ShopPage.ITEM_DRESS, ShopPage.BUTTON_ADD_TO_WISHLIST_DRESS, ShopPage.NAME_DRESS),
        (ShopPage.SECTION_EVENING_DRESSES, ShopPage.ITEM_EVENING_DRESS, ShopPage.BUTTON_ADD_TO_WISHLIST,
         ShopPage.NAME_EVENING_DRESS)]

    @pytest.mark.parametrize('section, '
                             'loc_item, '
                             'button_add_to_wishlist, '
                             'name_item',
                             testdata)
    def test_adding_items_in_wishlist(self,
                                      section,
                                      loc_item,
                                      button_add_to_wishlist,
                                      name_item):
        page.element_click(section)
        super().hover_to_click_hidden_button(loc_item, button_add_to_wishlist)
        super().wait_presence_element(ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST)

        assert page.get_elements_text(ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST) == Constants.ADDED_TO_WISHLIST, \
            'There is no window or note about adding to wishlist'

        page.element_click(ShopPage.BUTTON_CLOSE_WINDOW_NOTE_ADD_TO_WISHLIST)
        self.expected_wishlist_items.append(page.get_elements_text(name_item))

    def test_proper_name_of_wishlist_items(self):
        page.element_click(Wishlist.ACCOUNT)
        page.element_click(Wishlist.BUTTON_WISHLIST)

        assert page.find_need_element(Wishlist.WISHLIST_TABLE), 'Wishlist can\'t be found'
        assert page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS) == Constants.QUANTITY_ITEMS_IN_WISHLIST, \
            f'Expected quantity {Constants.QUANTITY_ITEMS_IN_WISHLIST} is not equal actual {page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS)}'

        page.element_click(Wishlist.NOTE_MY_WISHLIST)
        super().wait_presence_element(Wishlist.PLACE_WITH_ALL_ITEMS_IN_WISHLIST)
        actual_name_items_in_wishlist = []
        for i in Wishlist.LOCATORS_ITEMS_IN_WISHLIST:
            actual_name_items_in_wishlist.append(page.get_elements_text(i))

        assert actual_name_items_in_wishlist.sort() == self.expected_wishlist_items.sort(), \
            f'expected list {self.expected_wishlist_items} is not equal to actual {actual_name_items_in_wishlist}'
        # first method: import collections
        # assert collections.Counter(list_1) == collections.Counter(list_2), The lists l1 and l3 are not the same

    def test_save_proper_options_of_wishlist_items(self):
        # Choose quantity 3 of first item
        page.clear_value_in_box(Wishlist.OPTION_QUANTITY_OF_ITEMS)
        page.enter_value_into_box(Wishlist.OPTION_QUANTITY_OF_ITEMS, Constants.OPTION_QUANTITY_OF_ITEM_IN_WISHLIST)
        page.element_click(Wishlist.BUTTON_SAVE_OF_FIRST_ITEM)
        # Choose priority HIGH of second item
        page.element_click(Wishlist.OPTION_PRIORITY_OF_ITEM)
        page.element_click(Wishlist.BUTTON_SAVE_OF_SECOND_ITEM)
        # Delete third item
        page.element_click(Wishlist.BUTTON_DELETE_OF_THIRD_ITEM)
        super().refresh_page()

        assert page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS) == Constants.CHANGED_QUANTITY_ITEMS_IN_WISHLIST, \
            f'Expected quantity {Constants.CHANGED_QUANTITY_ITEMS_IN_WISHLIST} is not equal actual {page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS)}'
        page.element_click(Wishlist.NOTE_MY_WISHLIST)
        assert page.find_need_element(Wishlist.QUANTITY_OF_FIRST_ITEM), 'Can not find needed quantity of item'
        assert page.find_need_element(Wishlist.PRIORITY_OF_SECOND_ITEM), f'Priority is not {Constants.PRIORITY_HIGH}'
        assert not page.is_element_present(Wishlist.THIRD_ITEM), 'Third item is not deleted'

    def test_delete_wishlist(self):
        page.element_click(Wishlist.BUTTON_DELETE_WISHLIST)
        super().switch_to_alert_and_accept()
        super().wait_until_not_presence_element(Wishlist.TABLE_WISHLIST)

        assert not page.is_element_present(Wishlist.TABLE_WISHLIST), 'Wishlist is not deleted'

        page.element_click(Wishlist.BUTTON_HOME)

import pytest
from pages.wishlist_page import WishlistPageObject
from test_base import TestBase
from util.constants import Constants
from util.locators import Wishlist


class TestModuleWishlist(TestBase):
    expected_wishlist_items = []
    testdata = WishlistPageObject.get_test_data()

    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global main_page
        global wishlist_page
        main_page = super().get_main_page()
        wishlist_page = super().get_wishlist_page()

    def test_successful_login(self):
        super().log_in()
        super().check_proper_user()

    @pytest.mark.parametrize('item', testdata)
    def test_adding_items_in_wishlist(self, item):
        main_page.add_item_to_wishlist(item)
        assert main_page.get_notification_item_is_added_to_wishlist() == Constants.ADDED_TO_WISHLIST, \
            'There is no window or note about adding to wishlist'
        main_page.close_notification_item_is_added_to_wishlist()
        self.expected_wishlist_items.append(wishlist_page.get_wishlist_item_name(item))

    def test_proper_name_of_wishlist_items(self):
        main_page.go_to_wishlist()
        assert wishlist_page.get_wishlist_table(), 'Wishlist can\'t be found'
        assert wishlist_page.get_items_quantity_in_wishlist() == Constants.QUANTITY_ITEMS_IN_WISHLIST, \
            f'Expected quantity {Constants.QUANTITY_ITEMS_IN_WISHLIST} is not equal actual {wishlist_page.get_items_quantity_in_wishlist()}'
        wishlist_page.open_created_wishlist()
        actual_name_items_in_wishlist = []
        for i in Wishlist.LOCATORS_ITEMS_IN_WISHLIST:
            actual_name_items_in_wishlist.append(wishlist_page.get_elements_text(i))
        assert actual_name_items_in_wishlist.sort() == self.expected_wishlist_items.sort(), \
            f'expected list {self.expected_wishlist_items} is not equal to actual {actual_name_items_in_wishlist}'
        # first method: import collections
        # assert collections.Counter(list_1) == collections.Counter(list_2), The lists l1 and l3 are not the same

    def test_save_proper_options_of_wishlist_items(self):
        # Choose quantity 3 of first item
        wishlist_page.increase_items_count()
        # Choose priority HIGH of second item
        wishlist_page.choose_high_priority_for_item()
        # Delete third item
        wishlist_page.delete_item()
        assert wishlist_page.get_items_quantity_in_wishlist() == Constants.CHANGED_QUANTITY_ITEMS_IN_WISHLIST, \
            f'Expected quantity {Constants.CHANGED_QUANTITY_ITEMS_IN_WISHLIST} is not equal actual {wishlist_page.get_items_quantity_in_wishlist()}'
        wishlist_page.open_created_wishlist()
        assert wishlist_page.get_items_count(), 'Can not find needed quantity of item'
        assert wishlist_page.get_item_priority(), f'Priority is not {Constants.PRIORITY_HIGH}'
        assert not wishlist_page.is_item_present(), 'Third item is not deleted'

    def test_delete_wishlist(self):
        wishlist_page.remove_wishlist()
        assert not wishlist_page.is_wishlist_present(), 'Wishlist is not deleted'
        wishlist_page.go_home()

from pages.base_page import BasePage
from pages.item_page import ItemPageObject
from util.constants import Constants
from util.locators import Wishlist, ShopPage


class WishlistPageObject(BasePage):
    @staticmethod
    def get_test_data():
        return [
            ItemPageObject(ShopPage.SECTION_T_SHIRTS, ShopPage.ITEM_T_SHIRT, ShopPage.BUTTON_ADD_TO_WISHLIST,
                           ShopPage.NAME_T_SHIRT),
            ItemPageObject(ShopPage.SECTION_DRESSES, ShopPage.ITEM_DRESS, ShopPage.BUTTON_ADD_TO_WISHLIST_DRESS,
                           ShopPage.NAME_DRESS),
            ItemPageObject(ShopPage.SECTION_EVENING_DRESSES, ShopPage.ITEM_EVENING_DRESS,
                           ShopPage.BUTTON_ADD_TO_WISHLIST, ShopPage.NAME_EVENING_DRESS)
        ]

    def get_wishlist_table(self):
        return super().find_need_element(Wishlist.WISHLIST_TABLE)

    def get_items_quantity_in_wishlist(self):
        return super().get_elements_text(Wishlist.QUANTITY_OF_ITEMS)

    def open_created_wishlist(self):
        super().element_click(Wishlist.NOTE_MY_WISHLIST)
        super().wait_presence_element(Wishlist.PLACE_WITH_ALL_ITEMS_IN_WISHLIST)

    def increase_items_count(self):
        super().clear_value_in_box(Wishlist.OPTION_QUANTITY_OF_ITEMS)
        super().enter_value_into_box(Wishlist.OPTION_QUANTITY_OF_ITEMS, Constants.OPTION_QUANTITY_OF_ITEM_IN_WISHLIST)
        super().element_click(Wishlist.BUTTON_SAVE_OF_FIRST_ITEM)

    def choose_high_priority_for_item(self):
        super().element_click(Wishlist.OPTION_PRIORITY_OF_ITEM)
        super().element_click(Wishlist.BUTTON_SAVE_OF_SECOND_ITEM)

    def delete_item(self):
        super().element_click(Wishlist.BUTTON_DELETE_OF_THIRD_ITEM)
        super().refresh_page()

    def get_items_count(self):
        return super().find_need_element(Wishlist.QUANTITY_OF_FIRST_ITEM)

    def get_item_priority(self):
        return super().find_need_element(Wishlist.PRIORITY_OF_SECOND_ITEM)

    def is_item_present(self):
        return super().is_element_present(Wishlist.THIRD_ITEM)

    def remove_wishlist(self):
        super().element_click(Wishlist.BUTTON_DELETE_WISHLIST)
        super().switch_to_alert_and_accept()
        super().wait_until_not_presence_element(Wishlist.TABLE_WISHLIST)

    def is_wishlist_present(self):
        return super().is_element_present(Wishlist.TABLE_WISHLIST)

    def go_home(self):
        super().element_click(Wishlist.BUTTON_HOME)

    def get_wishlist_item_name(self, item):
        return super().get_elements_text(item.get_item_name())

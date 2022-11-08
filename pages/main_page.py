from pages.base_page import BasePage
from util.locators import ShopPage, MainPage, Wishlist


class MainPageObject(BasePage):
    def click_signin_button(self):
        super().element_click(MainPage.SIGNIN)

    def get_logged_user_name(self):
        return super().get_elements_text(MainPage.NAME_USER)

    def click_blouse_quick_view(self):
        super().hover_to_click_hidden_button(ShopPage.VIEW_PRODUCT_TOPS, ShopPage.BUTTON_QUICK_VIEW_BLOUSE)

    def choose_black_tops_filter(self):
        super().element_click(ShopPage.SECTION_WOMEN)
        super().element_click(ShopPage.CATEG_TOPS)
        super().element_click(ShopPage.COLOR_BLACK)

    def get_choosing_filters_log(self):
        return super().get_elements_text(ShopPage.CHOOSSING_FILTERS_LOGS)

    def get_black_color_attribute(self):
        return super().find_need_element(ShopPage.COLOR_BLACK_PRODUCT).get_attribute('href')

    def choose_midi_dress_filter(self):
        super().element_click(ShopPage.SECTION_WOMEN)
        super().element_click(ShopPage.CATEG_DRESSES)
        super().element_click(ShopPage.SUBCATEG_SUMMER_DRESSES)
        super().element_click(ShopPage.CHECKBOX_OF_MIDI_DRESS)

    def is_midi_dress_selected(self):
        return super().is_element_selected(ShopPage.CHECKBOX_OF_MIDI_DRESS_2)

    def get_filter_log(self):
        return super().get_elements_text(ShopPage.CHOOSSING_FILTERS_LOGS)

    def click_blouse_quick_view_in_dress(self):
        super().hover_to_click_hidden_button(ShopPage.VIEW_PRODUCT_DRESS, ShopPage.BUTTON_QUICK_VIEW_BLOUSE)

    def get_cart_items_count(self):
        return super().get_elements_text(ShopPage.NUMBER_ITEMS_IN_CART)

    def go_to_cart(self):
        super().element_click(ShopPage.CART)

    def wait_item_added_to_wishlist(self):
        super().wait_presence_element(ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST)

    def get_notification_item_is_added_to_wishlist(self):
        return super().get_elements_text(ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST)

    def close_notification_item_is_added_to_wishlist(self):
        super().element_click(ShopPage.BUTTON_CLOSE_WINDOW_NOTE_ADD_TO_WISHLIST)

    def go_to_wishlist(self):
        super().element_click(Wishlist.ACCOUNT)
        super().element_click(Wishlist.BUTTON_WISHLIST)

    def add_item_to_wishlist(self, item):
        super().element_click(item.get_section())
        super().hover_to_click_hidden_button(item.get_loc_item(), item.get_add_to_wishlist_button())
        self.wait_item_added_to_wishlist()

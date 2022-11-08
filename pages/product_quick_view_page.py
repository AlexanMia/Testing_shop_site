from pages.base_page import BasePage
from util.locators import ShopPage


class ProductQuickViewPageObject(BasePage):
    def find_frame(self):
        return super().find_need_element(ShopPage.FRAME)

    def switch_to_item_quick_view(self):
        super().switch_to_frame(ShopPage.FRAME)

    def choose_m_size_blouse(self):
        super().element_click(ShopPage.CHOOSING_SIZE_BLOUSE)
        super().element_click(ShopPage.SIZE_M_ARTICLE)

    def add_to_cart(self):
        super().element_click(ShopPage.BUTTON_ADD_TO_CART)

    def find_window_with_added_items(self):
        return super().find_need_element(ShopPage.WINDOW_WITH_ADDED_ITEMS)

    def wait_item_will_be_added_to_cart(self):
        super().wait_visibility_element(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)

    def get_text_about_successful_adding(self):
        return super().get_elements_text(ShopPage.TEXT_ABOUT_SUCCESSFUL_ADDING)

    def get_item_attribute_text(self):
        return super().get_elements_text(ShopPage.ATTRIBUTES_OF_ITEMS)

    def click_continue_shopping_button(self):
        super().element_click(ShopPage.BUTTON_CONTINUE_SHOPPING)

    def choose_m_size_dress(self):
        super().element_click(ShopPage.CHOOSING_SIZE_DRESS)
        super().element_click(ShopPage.SIZE_M_ARTICLE)
        super().element_click(ShopPage.COLOR_DRESS)

from pages.base_page import BasePage
from util.locators import Cart


class CartPageObject(BasePage):
    def increase_quantity_of_dresses(self):
        super().element_click(Cart.INCREASE_QUANTITY_OF_DRESSES)

    def are_items_in_the_cart(self):
        return super().find_need_element(Cart.BLOUSE) and super().find_need_element(Cart.PRINTED_CHIFFON_DRESS)

    def get_actual_items_count_in_the_cart(self):
        return super().find_need_element(Cart.ACTUAL_QUANTITY).get_attribute("value")

    def make_an_order(self):
        super().element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT)
        super().element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT_ADDRESS)
        super().element_click(Cart.AGREEMENT_WITH_TERMS)
        super().element_click(Cart.BUTTON_PROCEED_TO_CHECKOUT_SHIPPING)
        super().element_click(Cart.PAYMENT_BY_BANK_WIRE)
        super().element_click(Cart.BUTTON_CONFIRM_ORDER)

    def get_order_info(self):
        return super().get_elements_text(Cart.INFO_ABOUT_ORDER)

    def go_to_order(self):
        super().element_click(Cart.BUTTON_BACK_TO_ORDERS)

    def get_order_status(self):
        return super().get_elements_text(Cart.STATUS_OF_ORDER)

    def click_home_button(self):
        super().element_click(Cart.BUTTON_HOME)

import pytest
from pages.cart_page import CartPageObject
from pages.login_page import LoginPageObject
from pages.main_page import MainPageObject
from pages.product_quick_view_page import ProductQuickViewPageObject
from pages.wishlist_page import WishlistPageObject
from util.constants import Constants


class TestBase:
    @pytest.fixture(scope='class', autouse=True)
    def before_all(self, get_browser):
        global login_page
        global cart_page
        global quick_view_page
        global main_page
        global browser
        global wishlist_page
        browser = get_browser
        main_page = MainPageObject(browser, Constants.link_site)
        login_page = LoginPageObject(browser, Constants.link_site)
        quick_view_page = ProductQuickViewPageObject(browser, Constants.link_site)
        cart_page = CartPageObject(browser, Constants.link_site)
        wishlist_page = WishlistPageObject(browser, Constants.link_site)
        main_page.open()

    @staticmethod
    def get_main_page():
        return main_page

    @staticmethod
    def get_wishlist_page():
        return wishlist_page

    @staticmethod
    def get_cart_page():
        return cart_page

    @staticmethod
    def get_quick_view_page():
        return quick_view_page

    @staticmethod
    def log_in():
        main_page.click_signin_button()
        login_page.pass_login()
        login_page.pass_password()
        login_page.submit_signin()

    @staticmethod
    def check_proper_user():
        assert main_page.get_logged_user_name() == Constants.NAME_USER, \
            f"User's name is not {Constants.NAME_USER}"

from pages.base_page import BasePage
from util.constants import Constants
from util.locators import MainPage


class TestBase:
    def init_page(self, browser):
        global page
        page = BasePage(browser, Constants.link_site)
        return page

    def open_page(self):
        global page
        page.open()

    def get_to_log_in(self):
        global page
        page.element_click(MainPage.SIGNIN)
        page.enter_value_into_box(MainPage.LOG, Constants.EMAIL)
        page.enter_value_into_box(MainPage.PASSWORD, Constants.PASSWORD)
        page.element_click(MainPage.SIGNIN_BUTTON)

    def check_proper_user(self):
        # POINT 4
        global page
        assert page.get_elements_text(MainPage.NAME_USER) == Constants.NAME_USER, \
            f"User's name is not {Constants.NAME_USER}"

    # def is_element_present(self, locator):
    #     return self.find_need_element(locator)

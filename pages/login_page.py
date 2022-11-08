from pages.base_page import BasePage
from util.constants import Constants
from util.locators import MainPage


class LoginPageObject(BasePage):
    def pass_login(self):
        super().enter_value_into_box(MainPage.LOG, Constants.EMAIL)

    def pass_password(self):
        super().enter_value_into_box(MainPage.PASSWORD, Constants.PASSWORD)

    def submit_signin(self):
        super().element_click(MainPage.SIGNIN_BUTTON)

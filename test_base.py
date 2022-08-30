import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from util.constants import Constants
from util.locators import MainPage


class TestBase:
    @pytest.fixture(scope='class', autouse=True)
    def before_all(self, get_browser):
        global page
        global browser
        browser = get_browser
        page = BasePage(browser, Constants.link_site)
        page.open()

    @staticmethod
    def get_page():
        return page

    @staticmethod
    def log_in():
        page.element_click(MainPage.SIGNIN)
        page.enter_value_into_box(MainPage.LOG, Constants.EMAIL)
        page.enter_value_into_box(MainPage.PASSWORD, Constants.PASSWORD)
        page.element_click(MainPage.SIGNIN_BUTTON)

    @staticmethod
    def check_proper_user():
        assert page.get_elements_text(MainPage.NAME_USER) == Constants.NAME_USER, \
            f"User's name is not {Constants.NAME_USER}"

    @staticmethod
    def hover_to_click_hidden_button(locator_hover_element, locator_hidden_element):
        hover_element = page.find_need_element(locator_hover_element)
        hidden_button = page.find_need_element(locator_hidden_element)
        # hover element and click hidden button
        actions = ActionChains(browser)
        actions.move_to_element(hover_element)
        actions.click(hidden_button)
        actions.perform()

    @staticmethod
    def wait_presence_element(locator):
        WebDriverWait(browser, 15).until(EC.presence_of_element_located(locator))

    @staticmethod
    def wait_until_not_presence_element(locator):
        WebDriverWait(browser, 10).until_not(EC.presence_of_element_located(locator))

    @staticmethod
    def refresh_page():
        browser.refresh()

    @staticmethod
    def switch_to_alert_and_accept():
        browser.switch_to.alert.accept()

    @staticmethod
    def wait_visibility_element(locator):
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(locator))

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from util.constants import Constants
from util.locators import MainPage


class TestBase:
    def init_page(self, browser):
        global page
        page = BasePage(browser, Constants.link_site)
        return page

    def open_page(self):
        page.open()

    def log_in(self):
        page.element_click(MainPage.SIGNIN)
        page.enter_value_into_box(MainPage.LOG, Constants.EMAIL)
        page.enter_value_into_box(MainPage.PASSWORD, Constants.PASSWORD)
        page.element_click(MainPage.SIGNIN_BUTTON)

    def check_proper_user(self):
        assert page.get_elements_text(MainPage.NAME_USER) == Constants.NAME_USER, \
            f"User's name is not {Constants.NAME_USER}"

    def hover_to_click_hidden_button(self, browser, locator_hover_element, locator_hidden_element):
        # locators of elements: hover and hidden
        hover_element = page.find_need_element(locator_hover_element)
        hidden_button = page.find_need_element(locator_hidden_element)
        # hover element and click hidden button
        actions = ActionChains(browser)
        actions.move_to_element(hover_element)
        actions.click(hidden_button)
        actions.perform()

    def wait_presence_element(self, browser, locator):
        WebDriverWait(browser, 15).until(EC.presence_of_element_located(locator))

    def wait_until_not_presence_element(self, browser, locator):
        WebDriverWait(browser, 10).until_not(EC.presence_of_element_located(locator))
    def refresh_page(self, browser):
        browser.refresh()


    def switch_to_alert_and_accept(self, browser):
        browser.switch_to.alert.accept()


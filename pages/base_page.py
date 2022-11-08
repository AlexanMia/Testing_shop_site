from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def clear_value_in_box(self, locator):
        return self.find_need_element(locator).clear()

    def find_need_element(self, locator):
        return self.browser.find_element(*locator)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_elements_all(self, locator):
        return self.browser.find_elements(*locator)

    def element_click(self, locator):
        return self.find_need_element(locator).click()

    def enter_value_into_box(self, locator, meaning):
        return self.find_need_element(locator).send_keys(meaning)

    def get_elements_text(self, locator):
        return self.find_need_element(locator).text

    def switch_to_frame(self, locator):
        iframe = self.find_need_element(locator)
        self.browser.switch_to.frame(iframe)

    def switch_to_default_content(self):
        self.browser.switch_to.default_content()

    def is_element_selected(self, locator):
        return self.find_need_element(locator).is_selected()

    def hover_to_click_hidden_button(self, locator_hover_element, locator_hidden_element):
        hover_element = self.find_need_element(locator_hover_element)
        hidden_button = self.find_need_element(locator_hidden_element)
        # hover element and click hidden button
        actions = ActionChains(self.browser)
        actions.move_to_element(hover_element)
        actions.click(hidden_button)
        actions.perform()

    def wait_visibility_element(self, locator):
        WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located(locator))

    def wait_presence_element(self, locator):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(locator))

    def refresh_page(self):
        self.browser.refresh()

    def switch_to_alert_and_accept(self):
        self.browser.switch_to.alert.accept()

    def wait_until_not_presence_element(self, locator):
        WebDriverWait(self.browser, 10).until_not(EC.presence_of_element_located(locator))

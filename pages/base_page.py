from selenium.common.exceptions import NoSuchElementException


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

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def get_browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

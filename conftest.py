import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    #print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    #print("\nquit browser..")
    browser.quit()

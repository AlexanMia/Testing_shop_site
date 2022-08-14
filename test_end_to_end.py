import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_base import TestBase
from util.constants import Constants
from util.locators import ShopPage

from selenium.webdriver.support import expected_conditions as EC


class TestEndToEnd(TestBase):
    def test_open_site(self, browser):
        global page
        page = super().init_page(browser)
        super().open_page()

    def test_successful_login(self):
        super().get_to_log_in()
        super().check_proper_user()

    # choose some dresses
    def test_add_to_basket(self, browser):
    # go to WOMEN section
        global page
        page.element_click(ShopPage.SECTION_WOMEN)

    # go to Subcategories TOPS
        page.element_click(ShopPage.SUBCATEG_TOPS)

    # choose color of blouse
        page.element_click(ShopPage.COLOR_BLACK)
        #time.sleep(10)

        WebDriverWait(browser, 10).until(EC.presence_of_element_located(ShopPage.CHOOSSING_COLOR_BLACK))

        assert Constants.CHECKING_COLOR_BLACK.capitalize() in page.get_elements_text(ShopPage.CHOOSSING_COLOR_BLACK), \
            f'{Constants.CHECKING_COLOR_BLACK } is not chosen'

        assert Constants.CHECKING_COLOR_BLACK in page.find_need_element(ShopPage.COLOR_BLACK_PRODUCT).get_attribute('href'), \
        f'Choosing Color is not {Constants.CHECKING_COLOR_BLACK}'





        # ФРЕЙМ товара


        #page.element_click(ShopPage.VIEW_PRODUCT)

    # Поместите элементы, над которыми нужно навести курсор
        hover_element = page.find_need_element(ShopPage.VIEW_PRODUCT)
        hidden_bitton = page.find_need_element(ShopPage.BUTTON_QUICK_VIEW_BLOUSE)
    # Выполните операцию наведения на элемент
        actions = ActionChains(browser)
        actions.move_to_element(hover_element)
        #time.sleep(10)
        actions.click(hidden_bitton)
        actions.perform()

        time.sleep(10)

        page.switch_to_product_page(browser, ShopPage.FRAME)



        #
        page.element_click(ShopPage.CHOOSING_SIZE)
        #
        page.element_click(ShopPage.SIZE_M)
        # TODO ИНТЕРЕСУЕТ ЭТО МЕСТО, как он может не видеть фрейм?
        assert page.find_need_element(ShopPage.FRAME), 'Iframe is not be found'




   #
    #     # wait for Fastrack menu item to appear, then click it
    #     fastrack = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((ShopPage.BUTTON_QUICK_VIEW_BLOUSE)))
    #     fastrack.click()






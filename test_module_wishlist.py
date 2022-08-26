import datetime

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_base import TestBase
from util.constants import Constants
from util.locators import ShopPage, Wishlist


class TestModuleWishlist(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def open_site(self, browser):
        global page
        page = super().init_page(browser)
        super().open_page()

    def test_successful_login(self):
        super().log_in()
        super().check_proper_user()

    global names_items_add_to_wishlist
    names_items_add_to_wishlist = []

    @pytest.mark.parametrize('section, '
                             'loc_item, '
                             'button_add_to_wishlist, '
                             'window_and_note_add_to_wishlist, '
                             'text_added_to_wishlist, '
                             'close_note_about_adding, '
                             'name_item',
                             [(ShopPage.SECTION_T_SHIRTS,
                               ShopPage.ITEM_T_SHIRT,
                               ShopPage.BUTTON_ADD_TO_WISHLIST,
                               ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST,
                               Constants.ADDED_TO_WISHLIST,
                               ShopPage.BUTTON_CLOSE_WINDOW_NOTE_ADD_TO_WISHLIST,
                               ShopPage.NAME_T_SHIRT),
                              (ShopPage.SECTION_DRESSES,
                               ShopPage.ITEM_DRESS,
                               ShopPage.BUTTON_ADD_TO_WISHLIST_DRESS,
                               ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST,
                               Constants.ADDED_TO_WISHLIST,
                               ShopPage.BUTTON_CLOSE_WINDOW_NOTE_ADD_TO_WISHLIST,
                               ShopPage.NAME_DRESS),
                              (ShopPage.SECTION_EVENING_DRESSES,
                               ShopPage.ITEM_EVENING_DRESS,
                               ShopPage.BUTTON_ADD_TO_WISHLIST,
                               ShopPage.WINDOW_AND_NOTE_ADD_TO_WISHLIST,
                               Constants.ADDED_TO_WISHLIST,
                               ShopPage.BUTTON_CLOSE_WINDOW_NOTE_ADD_TO_WISHLIST,
                               ShopPage.NAME_EVENING_DRESS)])
    def test_adding_items_in_wishlist(self, browser,
                                      section,
                                      loc_item,
                                      button_add_to_wishlist,
                                      window_and_note_add_to_wishlist,
                                      text_added_to_wishlist,
                                      close_note_about_adding,
                                      name_item):
        page.element_click(section)
        super().hover_to_click_hidden_button(browser, loc_item, button_add_to_wishlist)
        assert page.get_elements_text(window_and_note_add_to_wishlist) == text_added_to_wishlist, \
            'There is not window or note about adding to wishlist'
        page.element_click(close_note_about_adding)
        names_items_add_to_wishlist.append(page.get_elements_text(name_item))

    def test_proper_name_of_items(self, browser):
        page.element_click(Wishlist.ACCOUNT)
        page.element_click(Wishlist.BUTTON_WISHLIST)
        assert page.find_need_element(Wishlist.WISHLIST), 'Wishlist can\'t be found'
        assert page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS) == Constants.QUANTITY_ITEMS_IN_WISHLIST, \
            f'Expected quantity {Constants.QUANTITY_ITEMS_IN_WISHLIST} is not equal actual {page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS)}'
        page.element_click(Wishlist.NOTE_MY_WISHLIST)
        WebDriverWait(browser, 15).until(EC.presence_of_element_located(Wishlist.PLACE_WITH_ALL_ITEMS_IN_WISHLIST))
        actual_name_items_in_wishlist = []
        locators_items_in_wishlist = [Wishlist.FIRST_ITEMS_T_SHIRT_IN_WISHLIST,
                                      Wishlist.SECOND_ITEMS_DRESS_IN_WISHLIST,
                                      Wishlist.THIRD_ITEMS_EVENING_DRESS_IN_WISHLIST]
        for i in locators_items_in_wishlist:
            actual_name_items_in_wishlist.append(page.get_elements_text(i))
        assert actual_name_items_in_wishlist.sort() == names_items_add_to_wishlist.sort(), \
            f'expected list {names_items_add_to_wishlist} is not equal actual {actual_name_items_in_wishlist}'
        # первый способ import collections
        # assert collections.Counter(list_1) == collections.Counter(list_2), The lists l1 and l3 are not the same

    def test_save_proper_options_of_items(self, browser):
        page.clear_value_in_box(Wishlist.OPTION_QUANTITY_OF_ITEMS)
        page.enter_value_into_box(Wishlist.OPTION_QUANTITY_OF_ITEMS, Constants.OPTION_QUANTITY_OF_ITEM_IN_WISHLIST)
        page.element_click(Wishlist.BUTTON_SAVE_OF_FIRST_ITEM)
        # у второго товара выбрать приоритет HIGH
        page.element_click(Wishlist.OPTION_PRIORITY_OF_ITEM)
        page.element_click(Wishlist.BUTTON_SAVE_OF_SECOND_ITEM)
        # третий товар удаляем, нажать на кнопку
        page.element_click(Wishlist.BUTTON_DELETE_OF_THIRD_ITEM)
        browser.refresh()
        assert page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS) == Constants.CHANGED_QUANTITY_ITEMS_IN_WISHLIST, \
            f'Expected quantity {Constants.CHANGED_QUANTITY_ITEMS_IN_WISHLIST} is not equal actual {page.get_elements_text(Wishlist.QUANTITY_OF_ITEMS)}'
        page.element_click(Wishlist.NOTE_MY_WISHLIST)
        assert page.find_need_element(Wishlist.QUANTITY_OF_FIRST_ITEM), 'Can not find needed quantity of item'
        assert page.find_need_element(Wishlist.PRIORITY_OF_SECOND_ITEM), f'Priority is not {Constants.PRIORITY_HIGH}'
        assert not page.is_element_present(Wishlist.THIRD_ITEM), 'Third item is not deleted'

    def test_delete_wishlist(self, browser):
        start = datetime.datetime.now()
        print(start)

        page.element_click(Wishlist.BUTTON_DELETE_WISHLIST)
        now = datetime.datetime.now()
        print('I finished', now)

        browser.switch_to.alert.accept()
        now = datetime.datetime.now()
        print('I am here', now)

        WebDriverWait(browser, 10).until_not(EC.presence_of_element_located(Wishlist.TABLE_WISHLIST))
        now = datetime.datetime.now()
        print('Now I am here', now)

        assert not page.is_element_present(Wishlist.TABLE_WISHLIST), 'Wishlist is not deleted'
        now = datetime.datetime.now()
        print('Buy', now)

        page.element_click(Wishlist.BUTTON_HOME)
        finish = datetime.datetime.now()
        print(finish)
        # END

from selenium.webdriver.common.keys import Keys

from helper.wait import wait_for_search_result_page_to_load
from lib.locators import HomePageLocators
from lib.page_objects.base_po import BasePage


class HomePage(BasePage):
    elements = {}

    def __init__(self, context):
        super().__init__(context.browser)

    def search_for_item(self, item):
        search_field = self.find_element(*HomePageLocators.SEARCH_FIELD)
        self.write_text(search_field, item)
        search_field.send_keys(Keys.ENTER)

        wait_for_search_result_page_to_load(self.browser)


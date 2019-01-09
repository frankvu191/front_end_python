from lib.locators import SearchResultPageLocators
from lib.page_objects.base_po import BasePage


class SearchResultPage(BasePage):

    def __init__(self, context):
        super().__init__(context.browser)

    def get_result_count_text(self):
        result_count_text = (self.find_element(*SearchResultPageLocators.RESULT_COUNT_TEXT)).text

        return result_count_text

    def get_result_count(self):
        result_count = self.find_elements(*SearchResultPageLocators.RESULT_COUNT)

        return result_count


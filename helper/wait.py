from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lib.locators import HomePageLocators, SearchResultPageLocators


def wait_for_home_page_to_load(driver):
    try:
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(HomePageLocators.SEARCH_FIELD))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(HomePageLocators.SEARCH_BUTTON))

    except TimeoutException:
        print('Home page is not fully loaded.')


def wait_for_search_result_page_to_load(driver):
    try:
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(SearchResultPageLocators.RESULT_COUNT_TEXT))
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(SearchResultPageLocators.RESULT_COUNT))

    except TimeoutException:
        print('Search result page is not fully loaded.')

from selenium.webdriver.common.by import By


class HomePageLocators(object):

    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[value='Go']")


class SearchResultPageLocators(object):

    RESULT_COUNT_TEXT = (By.CSS_SELECTOR, "span[id='s-result-count']")
    RESULT_COUNT = (By.CSS_SELECTOR, "li[id^='result']")

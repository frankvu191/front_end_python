import time

from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 20

    def find_element(self, *loc):
        return self.browser.find_element(*loc)

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        # Hover is sensitive and needs some sleep time
        time.sleep(5)

    def javascript_click(self, element):
        self.browser.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.browser.current_url

    def find_elements(self, *loc):
        return self.browser.find_elements(*loc)

    def write_text(self, element, text):
        element.clear()
        element.send_keys(text)

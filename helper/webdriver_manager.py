# import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def set_up_driver(context):
    # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['BROWSER']
    else:
        browser = 'chrome'

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        # for running in headless mode
        options.add_argument("--headless")
        context.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

        # executable_path = base_dir + DataFactory.chrome_driver
        # context.browser = webdriver.Chrome(executable_path=executable_path)

    elif browser == 'firefox':
        context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'safari':
        context.browser = webdriver.Safari()
    elif browser == 'ie':
        context.browser = webdriver.Ie()
    elif browser == 'opera':
        context.browser = webdriver.Opera()
    elif browser == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", browser, "is invalid value")

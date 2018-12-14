# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()
import os
import shutil
import time
import logging

from helper.webdriver_manager import *


def before_all(context):
    set_up_driver(context)


def before_feature(context, feature):
    # Create logger
    # TODO - http://stackoverflow.com/questions/6386698/using-the-logging-python-class-to-write-to-a-file
    context.logger = logging.getLogger('seleniumframework_tests')
    hdlr = logging.FileHandler('./seleniumframework_tests.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    context.logger.addHandler(hdlr)
    context.logger.setLevel(logging.DEBUG)


def before_scenario(context, scenario):
    pass


def before_tag(context, tag):
    pass


def after_scenario(context, scenario):
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
            os.chdir("failed_scenarios_screenshots")
            context.browser.save_screenshot(scenario.name + "_failed.png")


def after_feature(context, feature):
    pass


def after_all(context):
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("failed_scenarios_screenshots"):
            os.rmdir("failed_scenarios_screenshots")
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
            # os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")

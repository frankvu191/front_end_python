from behave import given, when, then

from helper.wait import *
from lib.datafactory import DataFactory
from lib.page_objects.home_po import HomePage
from lib.page_objects.search_result_po import SearchResultPage


@given('I am in Amazon home page')
def step_impl(context):
    context.home_page = HomePage(context)
    context.home_page.visit(DataFactory.base_url)
    wait_for_home_page_to_load(context.browser)
    context.search_result_page = SearchResultPage(context)


@when('I search for "{item}"')
def step_impl(context, item):
    context.search_item = item
    context.home_page.search_for_item(item)


@then('I should see more than "{result}" result displayed')
def step_impl(context, result):
    assert(context.search_item in context.search_result_page.get_result_count_text())
    assert(len(context.search_result_page.get_result_count()) > int(result))

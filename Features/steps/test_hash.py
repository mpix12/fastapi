from behave import *

use_step_matcher("re")


@given("I am on Blog docs page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('STEP: Given I am on Blog docs page')


@when("I use page as 5")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('STEP: When I use page as 5')


@step("page_size as 10")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('STEP: And page_size as 10')


@step("Execute /blog/all_details")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('STEP: And Execute /blog/all_details')


@then("I should get response as 200")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('STEP: Then I should get response as 200')
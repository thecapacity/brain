from app import app
from behave import given, when, then
from behave import use_step_matcher

use_step_matcher("re")

@given(u'the Flask app is running')
def step_impl(context):
    context.client = app.test_client()

@when(u'I visit the home page')
def step_impl(context):
    context.response = context.client.get('/')

@then(u'I should see "(.*)"')
def step_impl(context, expected_text = None):
    assert expected_text.encode() in context.response.data, f"Expected '{expected_text}' in response"


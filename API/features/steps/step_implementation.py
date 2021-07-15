import requests
from behave import *

from payLoad import addbook_payload
from utilities.configuration import get_config, get_password
from utilities.resourses import APIResources


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.headers = {"Content-Type": "application/json;charset=UTF-8"}
    context.url_add = get_config()['API']['endpoint'] + APIResources.addBook
    context.payload = addbook_payload("Example", 123)


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response_add = requests.post(context.url_add, json=context.payload, headers=context.headers,)


@then('Book is successfully added')
def step_impl(context):
    context.addbook = context.response_add.json()
    print(context.addbook)
    context.bookID = context.addbook['ID']
    message = context.addbook['Msg']
    assert message == "successfully added"


@given('the Book details with {isbn} and {aisle} which needs to be added to Library')
def step_impl(context, isbn, aisle):
    context.headers = {"Content-Type": "application/json;charset=UTF-8"}
    context.url_add = get_config()['API']['endpoint'] + APIResources.addBook
    context.payload = addbook_payload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('rupeshmodak', get_password())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(APIResources.github_url)


@then('Status code of response should be {StatusCode:d}')
def step_impl(context, StatusCode):
    print(context.response.status_code)
    assert context.response.status_code == StatusCode


# from behave import given, when, then
# import requests
# import json
#
#
# api_url = 'https://api.duckduckgo.com'
#
# @when('the DuckDuckGo API is queried with')
# def step_when_the_duckduckgo_api_is_queried_with(context):
#     context.api_url = api_url
#     for row in context.table:
#         phrase = row['phrase']
#         format = row['format']
#         params = {
#             'q': phrase,
#             'format': format,
#         }
#         context.response = requests.get(context.api_url, params=params)
#
# @then('the response status code is "{expected_status_code}"')
# def step_then_the_response_status_code_is(context, expected_status_code):
#     assert str(context.response.status_code) == expected_status_code
#
# @then('the response contains results for "{phrase}"')
# def step_then_the_response_contains_results_for(context, phrase):
#     response_content = json.loads(context.response.content)
#     assert 'Heading' in response_content
#     assert response_content['Heading'].lower() == phrase.lower()

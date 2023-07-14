# import requests
# from pytest_bdd import scenarios, given, when, then, parsers
#
# DUCKDUCKGO_API = "https://api.duckduckgo.com"
#
# scenarios('../features/service.feature')
#
# @given('the DuckDuckGo API is queried with "<phrase>" using "json" format', target_fixture="ddg_response")
# def api_query(phrase):
#     params = {
#         'q': phrase,
#         'format': 'json',
#     }
#     response = requests.get(DUCKDUCKGO_API, params=params)
#     return response
#
# @then('the response status code is "200"')
# def response_code_is_200(ddg_response):
#     assert ddg_response.status_code == 200
#
# @then(parsers.parse('the response contains results for "<phrase>"'))
# def response_contains_results(ddg_response, phrase):
#     json_body = ddg_response.json()
#     assert phrase.lower() in json_body["Heading"].lower()

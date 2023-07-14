# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# @given('the DuckDuckGo home page is displayed')
# def step_given_the_duckduckgo_home_page_is_displayed(context):
#     context.driver = webdriver.Edge()  # Replace with the driver of your choice
#     context.driver.get('https://duckduckgo.com')
#
# @when('the user searches for "{phrase}"')
# def step_when_the_user_searches_for(context, phrase):
#     search_box = context.driver.find_element_by_id('search_form_input_homepage')
#     search_box.send_keys(phrase + Keys.RETURN)
#
# @when('the user searches for the phrase')
# def step_when_the_user_searchs_for_phrase(context):
#     phrase = context.text  # context.text holds the multi-line text
#     search_box = context.driver.find_element_by_id('search_form_input_homepage')
#     search_box.send_keys(phrase + Keys.RETURN)
#
# @then('results are shown for "{phrase}"')
# def step_then_results_are_shown_for(context, phrase):
#     results = context.driver.find_elements_by_class_name('result')
#     assert any(phrase.lower() in result.text.lower() for result in results)
#     context.driver.quit()
#
# @then('one of the results contains "{phrase}"')
# def step_then_results_contains(context, phrase):
#     results = context.driver.find_elements_by_class_name('result')
#     assert any(phrase.lower() in result.text.lower() for result in results)
#     context.driver.quit()

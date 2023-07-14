# from pytest_bdd import scenarios, given, when, then, parsers
#
# from cucumbers import CucumberBasket
#
# # Constants
# MAX_CUCUMBERS = 10
#
# # Scenarios
# scenarios('../features/unit_outlines.feature')
#
#
# # Given Steps
# @given(parsers.parse('the basket has "<initial>" cucumbers'), target_fixture="basket")
# def basket(initial):
#     return CucumberBasket(int(initial))
#
# # When Steps
# @when(parsers.parse('"<some>" cucumbers are added to the basket'))
# def add_cucumbers(basket, some):
#     basket.add(int(some))
#
# @when(parsers.parse('"<some>" cucumbers are removed from the basket'))
# def remove_cucumbers(basket, some):
#     basket.remove(int(some))
#
# # Then Steps
# @then(parsers.parse('the basket contains "<total>" cucumbers'))
# def basket_has_total(basket, total):
#     assert basket.count == int(total)

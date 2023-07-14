# import pytest
# from pytest_bdd import scenarios, given, when, then, parsers
#
# from cucumbers import CucumberBasket
#
# MAX_CUCUMBERS = 10
#
# scenarios('../features/unit_basic.feature')
#
# @pytest.fixture
# def basket():
#     return CucumberBasket()
#
# @given(parsers.parse('the basket has "{initial:d}" cucumber'))
# @given(parsers.parse('the basket has "{initial}" cucumbers'))
# def the_basket_has_cucumbers(basket, initial):
#     basket.add(int(initial))
#
# @given('the basket is empty')
# def the_basket_is_empty(basket):
#     basket.remove(basket.count)
#
# @given('the basket is full')
# def the_basket_is_full(basket):
#     while basket.count < MAX_CUCUMBERS:
#         basket.add(1)
#
# @when(parsers.parse('"{quantity}" cucumbers are added to the basket'))
# def cucumbers_are_added_to_the_basket(basket, quantity):
#     basket.add(int(quantity))
#
# @when(parsers.parse('"{quantity}" cucumbers are removed from the basket'))
# def cucumbers_are_removed_from_the_basket(basket, quantity):
#     basket.remove(int(quantity))
#
# @then(parsers.parse('the basket contains "{final}" cucumbers'))
# def the_basket_contains_cucumbers(basket, final):
#     assert basket.count == int(final)
#
# @then('the basket is empty')
# def the_basket_is_empty(basket):
#     assert basket.count == 0
#
# @then('the basket is full')
# def the_basket_is_full(basket):
#     assert basket.count == MAX_CUCUMBERS
#
# @then(parsers.parse('"{quantity}" cucumbers cannot be added to the basket'))
# def cucumbers_cannot_be_added_to_the_basket(basket, quantity):
#     with pytest.raises(ValueError):
#         basket.add(int(quantity))
#
# @then(parsers.parse('"{quantity}" cucumbers cannot be removed from the basket'))
# def cucumbers_cannot_be_removed_from_the_basket(basket, quantity):
#     with pytest.raises(ValueError):
#         basket.remove(int(quantity))
#
# @when(parsers.parse('"{quantity}" more cucumbers are added to the basket'))
# def more_cucumbers_are_added_to_the_basket(basket, quantity):
#     basket.add(int(quantity))

# from behave import given, when, then
# from cucumbers import CucumberBasket
#
# @given('the basket has "{initial:d}" cucumber')
# @given('the basket has "{initial}" cucumbers')
# def step_given_the_basket_has_cucumbers(context, initial):
#     context.basket = CucumberBasket()
#     context.basket.add(int(initial))
#
# @given('the basket is empty')
# def step_given_the_basket_is_empty(context):
#     context.basket = CucumberBasket()
#
# @given('the basket is full')
# def step_given_the_basket_is_full(context):
#     context.basket = CucumberBasket()
#     context.basket.add(10)
#
# @when('"{some}" cucumbers are added to the basket')
# def step_when_cucumbers_are_added_to_the_basket(context, some):
#     context.basket.add(int(some))
#
# @when('"{some}" cucumbers are removed from the basket')
# def step_when_cucumbers_are_removed_from_the_basket(context, some):
#     context.basket.remove(int(some))
#
# @then('the basket contains "{total}" cucumbers')
# def step_then_the_basket_contains_cucumbers(context, total):
#     assert context.basket.count == int(total)
#
# @then('the basket is full')
# def step_then_the_basket_is_full(context):
#     assert context.basket.full
#
# @then('the basket is empty')
# def step_then_the_basket_is_empty(context):
#     assert context.basket.empty
#
# @then('"{some}" cucumbers cannot be added to the basket')
# def step_then_cucumbers_cannot_be_added_to_the_basket(context, some):
#     try:
#         context.basket.add(int(some))
#         assert False, "Expected an error when overfilling the basket"
#     except ValueError:
#         pass
#
# @then('"{some}" cucumbers cannot be removed from the basket')
# def step_then_cucumbers_cannot_be_removed_from_the_basket(context, some):
#     try:
#         context.basket.remove(int(some))
#         assert False, "Expected an error when removing too many cucumbers from the basket"
#     except ValueError:
#         pass
#
# # Additional steps for the add and remove scenario
#
# @when('"{some}" more cucumbers are added to the basket')
# def step_when_more_cucumbers_are_added_to_the_basket(context, some):
#     context.basket.add(int(some))
#

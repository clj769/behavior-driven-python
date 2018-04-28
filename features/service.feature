@service @duckduckgo
Feature: DuckDuckGo Instant Answer API
  As an application developer,
  I want to get instant answers for search terms via a REST API,
  So that I can get answers anywhere in my app.

  # It is popular practice to use imperative steps for service API testing.
  # Karate does this: https://github.com/intuit/karate
  # However, better BDD practice is to use declarative steps.
  # This allows greater code reuse in the automation code.

  Scenario Outline: Basic DuckDuckGo API Query
    When the DuckDuckGo API is queried for "<phrase>" in "json"
    Then the response status code is "200"
    And the response contains results for "<phrase>"

    Examples: Animals
      | phrase   |
      | panda    |
      | python   |
      | platypus |

    Examples: Fruits
      | phrase     |
      | peach      |
      | pineapple  |
      | papaya     |

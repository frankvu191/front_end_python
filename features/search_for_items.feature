@search_for_items
Feature: Search for items

  @search_for_existing_items
  Scenario: Search for existing items
    Given I am in Amazon home page
    When I search for "Kindle"
    Then I should see more than "1" result displayed
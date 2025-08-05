@api
Feature: Brand list management should reject unsupported operations

  Scenario: I attempt to update the brand list using an unsupported method
    When I try to update the brands list using an unsupported method
    Then I should receive a method not allowed error
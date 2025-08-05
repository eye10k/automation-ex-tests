@api
Feature: Registering a new user account via API

  Scenario: I successfully register a new user through the API
    Given I am a new visitor without an account
    When I register with valid personal and contact details
    Then my account should be successfully registered
    And I should be able to retrieve my account details by email
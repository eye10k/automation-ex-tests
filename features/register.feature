@ui
Feature: Register and order as a new user

  Scenario: I register during checkout and successfully place an order
    When I add products to my cart
    And I go to my cart
    Then I should see my cart

    When I proceed to checkout
    And I choose to register a new account
    And I sign up and create my account
    Then I should see the message "ACCOUNT CREATED!"
    When I continue from the account created page
    Then I should be logged in as my user

    When I go back to my cart
    And I confirm the checkout
    Then I should see my address and order details

    When I leave a comment and place my order
    And I provide my payment details
    And I confirm the payment

    Then I should see the message "Your order has been placed successfully!"

    When I delete my account
    Then I should see the message "ACCOUNT DELETED!"
    And I finish by clicking Continue

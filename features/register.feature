@ui
Feature: Register and order as a new user

  Scenario: I register during checkout and successfully place an order
    Given I navigate to the home page
    When I add products to my cart
    And I go to my cart
    Then I should see my cart

    When I proceed to checkout
    And I choose to register a new account
    And I sign up and create my account
    Then I should see the message "ACCOUNT CREATED!" and I am logged in

    When I go back to my cart
    And I confirm the checkout
    Then I should see my address and order details

    When I leave a comment and place my order
    And I provide my payment details

    Then I should see success message "Congratulations! Your order has been confirmed!"

    When I delete my account
    Then I should see the message "Account Deleted!"
    And I finish by clicking Continue

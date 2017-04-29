Feature: Compute factorial
  In order to play with Lettuce
  As beginners
  We'll implement factorial

  Scenario: Factorial of 0
    Given I have the number 0
    When I compute its factorial
    Then I see the number 1

  Scenario: Factorial of 1
    Given I have the number 1
    When I compute its factorial
    Then I see the number 1

  Scenario: Factorial of 2
    Given I have the number 2
    When I compute its factorial
    Then I see the number 2

  Scenario: Factorial of 3
    Given I have the number 3
    When I compute its factorial
    Then I see the number 6
Feature: Register user

  @NotImplementedYet
  Scenario: register user in redmine
    Given Setup chrome driver
    And I connect to redmine
    When I register a user in redmine
    Then I validate I'm logged in with the registered user

    Examples:
      | user               | password             | valid  |
      | maximilianomikkan  | cardaABC123          | true   |
      | mmikkan            | cardaABC123          | true   |


  @Broken
  Scenario: register existen user in redmine
    Given Setup chrome driver
    And I connect to redmine
    When I register an existen user in redmine
    Then I validate user is not created

    Examples:
      | user               | password             | valid  |
      | maximilianomikkan  | cardaABC123          | true   |
      | mmikkan            | cardaABC123          | true   |
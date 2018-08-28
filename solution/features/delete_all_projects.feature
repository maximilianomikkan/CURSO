Feature: delete all projects

  Scenario Outline: delete all projects
    Given Setup chrome driver
    And I connect to redmine
    When I login as user into redmine with '<user>' and '<password>'
    And I validate I'm logged in '<valid>'
    And I delete all projects
    Then I validate all projects were deleted

    Examples:
      | user               | password       | valid  |
      #| maximilianomikkan  | cardaABC123    | true   |
      | mmikkan            | cardaABC123    | true  |
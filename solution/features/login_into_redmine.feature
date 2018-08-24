Feature: Login into Redmine

  Scenario Outline: login into redmine
    Given Setup chrome driver
    And I connect to redmine
    When I login as '<valid>' user into redmine with '<user>' and '<password>'
    Then Validate I'm logged in

    Examples:
      | user               | password             | valid  |
      |                    |                      | false  |
      |                    | cardaABC123          | false  |
      | maximilianomikkan  |                      | false  |
      | wrong_user         | cardaABC123          | false  |
      | maximilianomikkan  | wrong_password       | false  |
      | maximilianomikkan  | cardaABC123          | true   |

#Feature: Login into Redmine
#
#  Scenario Outline: login into redmine
#    Given Setup chrome driver
#    And I connect to redmine
#    When I login as '<valid>' user into redmine with '<user>' and '<password>'
#    Then Validate I'm logged in
#
#    Examples:
#      | user               | password             | valid  |
#      | maximilianomikkan  | cardaABC123          | true   |
#      |                    |                      | false  |
#      |                    | cardaABC123          | false  |
#      | maximilianomikkan  |                      | false  |
#      | wrong_user         | cardaABC123          | false  |
#      | maximilianomikkan  | wrong_password       | false  |
#      | maximilianomikkan  | cardaABC123          | true   |

Feature: Login into Redmine and Create a Project

  Scenario Outline: login into redmine and create a project
    Given Setup chrome driver
    And I connect to redmine
    When I login as user into redmine with '<user>' and '<password>'
    Then I validate I'm logged in '<valid>'

    Examples:
      | user               | password             | valid  |
#      | maximilianomikkan  | cardaABC123          | true   |
      | wrong_user         | cardaABC123          | false  |
      | maximilianomikkan  | wrong_password       | false  |
      |                    |                      | false  |
      |                    | cardaABC123          | false  |
      | maximilianomikkan  |                      | false  |

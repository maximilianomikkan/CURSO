

Feature: Login into Redmine

  Scenario Outline: login into redmine and create a project
    Given Setup chrome driver
    And I connect to redmine
    When I login as user into redmine with '<user>' and '<password>'
    Then I validate I'm logged in '<valid>'

    Examples:
      | user               | password             | valid  |
      | empty              | empty                | false  |
      | empty              | cardaABC123          | false  |
      | maximilianomikkan  | empty                | false  |
      | wrong_user         | cardaABC123          | false  |
      | maximilianomikkan  | wrong_password       | false  |
      | maximilianomikkan  | cardaABC123          | true   |

#Feature: Login into Redmine and Create a Project

#  Scenario Outline: login into redmine and create a project
#    Given Setup chrome driver
#    And I connect to redmine
#    When I login as user into redmine with '<user>' and '<password>'
#    Then I validate I'm logged in '<valid>'
#
#    Examples:
#      | user       | password         | valid  |
#      |            |                  | false  |
#      |            | cardaABC123      | false  |
#      | mmikkan    |                  | false  |
#      | wrong_user | cardaABC123      | false  |
#      | mmikkan    | wrong_password   | false  |
#      | mmikkan    | cardaABC123      | true   |
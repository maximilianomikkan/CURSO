Feature: Login into Redmine and Create a Project

  Scenario Outline: login into redmine and create a project
    Given Setup chrome driver
    And I connect to redmine
    When I login as '<valid>' user with into redmine with '<user>' and '<password>'
    And I create a project
    Then Validate Project was created

    Examples:
      | user               | password             | valid  |
      |                    |                      | false  |
      |                    | cardaABC123          | false  |
      | maximilianomikkan  |                      | false  |
      | wrong_user         | cardaABC123          | false  |
      | maximilianomikkan  | wrong_password       | false  |
      | maximilianomikkan  | cardaABC123          | true   |

#    Examples:
#      | user               | password             | valid  |
#      |                    |                      | false  |
#      |                    | cardaABC123          | false  |
#      | mmikkan            |                      | false  |
#      | wrong_user         | cardaABC123          | false  |
#      | mmikkan            | wrong_password       | false  |
#      | mmikkan            | cardaABC123          | true   |
#








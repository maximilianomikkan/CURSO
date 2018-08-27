Feature: Login into Redmine and Create a Project

  Scenario Outline: login into redmine and create a project
    Given Setup chrome driver
    And I connect to redmine
    When I login as user into redmine with '<user>' and '<password>'
    And I validate I'm logged in
    And I create a project
    Then Validate Project was created

    Examples:
      | user               | password             | valid  |
      | maximilianomikkan  | cardaABC123          | true   |
      | wrong_user         | cardaABC123          | false  |
      | maximilianomikkan  | wrong_password       | false  |
#      |                    |                      | false  |
#      |                    | cardaABC123          | false  |
#      | maximilianomikkan  |                      | false  |



#    Examples:
#      | user               | password             | valid  |
#      |                    |                      | false  |
#      |                    | cardaABC123          | false  |
#      | mmikkan            |                      | false  |
#      | wrong_user         | cardaABC123          | false  |
#      | mmikkan            | wrong_password       | false  |
#      | mmikkan            | cardaABC123          | true   |
#








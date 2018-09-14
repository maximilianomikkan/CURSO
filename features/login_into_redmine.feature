Feature: Login into Redmine

  @Working
  Scenario Outline: invalid login into redmine
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
      | mmikkan  | cardaABC123          | true   |

  @Working
  Scenario Outline: valid login into redmine
    Given Setup chrome driver
    And I connect to redmine
    When I login as user into redmine with '<user>' and '<password>'
    Then I validate I'm logged in '<valid>'

    Examples:
      | user               | password             | valid  |
      #| maximilianomikkan  | cardaABC123          | true   |
      | mmikkan            | cardaABC123          | true   |
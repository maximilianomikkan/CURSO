Feature: Login into Redmine and Create a Project

  @Working
  Scenario Outline: login into redmine and create a project
    Given Setup chrome driver
    And I connect to redmine
    When I login as user into redmine with '<user>' and '<password>'
    And I validate I'm logged in '<valid>'
    Then I create a project
    And Validate Project was created

    Examples:
      | user               | password       | valid  |
      #| maximilianomikkan  | cardaABC123    | true   |
      | mmikkan            | cardaABC123    | true  |





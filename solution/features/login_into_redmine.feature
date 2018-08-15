Feature: Login into Redmine

  Scenario: login into redmine
    Given Setup chrome driverq
    And I connect to redmineq
    When I login into redmineq
      | user              | password            |
      #| maximilianomikkan | cardaABC123         |
      | mmikkan           | cardaABC123         |
    Then Validate I'm logged inq

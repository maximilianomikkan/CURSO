Feature: Login into Redmine

  Scenario: login into redmine
    Given Setup chrome driver
    And I connect to redmine
    When I login into redmine
      | user              |  password           |
      | maximilianomikkan | cardaABC123         |
    Then Validate I'm logged in

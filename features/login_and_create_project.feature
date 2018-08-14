Feature: Login into Redmine and Create a Project

  Scenario: login into redmine and create a project
    Given Setup chrome driver
    And I connect to redmine
    When I login into redmine
      | user              | password            |
      | maximilianomikkan | cardaABC123         |
      #| mmikkan           | cardaABC123         |
    And I create a project
    Then Validate Project was created

Feature: Login into TMS Angular

  Scenario: login into tmsangular
    Given Setup chrome driver
    And I connect to tmsangular
    When I login into tmsangular
      | user              | password            |
      | mmikkan           | bongOrno456         |
    Then Validate I'm logged in

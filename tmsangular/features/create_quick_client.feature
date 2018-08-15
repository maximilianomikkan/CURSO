Feature: Create Quick Client

  Scenario: create quick client
    Given Setup chrome driver
    And I connect to tmsangular
    When I login into tmsangular
      | user              | password            |
      | mmikkan           | bongOrno456         |
    And Validate I'm logged inq
    Then Create Quick Client

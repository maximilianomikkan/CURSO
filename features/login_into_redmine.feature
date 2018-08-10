Feature: Login into Redmine

  Scenario: login into redmine

     Given completo el formulario
      When le doy click al boton
      Then veo el home

    Scenario:
    Given Setup chrome driver
      And I connect to redmine
      When I login into redmine
      Then Validate I'm logged in

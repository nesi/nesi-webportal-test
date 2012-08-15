Feature: NeSI Login

  Scenario: Test logging in
    _LOGIN_ Given I go to the NeSI login page
    _LOGIN_ And set <username> as username
    _LOGIN_ And set <password> as password
    _LOGIN_ And click the login button
    _LOGIN_ Then I am logged in
    _LOGOUT_ I can log out

    Examples:
      | username | password |
      | m.feller@auckland.ac.nz |  test123 |

  Scenario: Test failure to log in
    _LOGIN_ Given I go to the NeSI login page
    _LOGIN_ And set <username> as username
    _LOGIN_ And set <password> as password
    _LOGIN_ And click the login button
    _LOGIN_ Then I am not logged in

    Examples:
      | username | password |
      | m.feller@auckland.ac.nz | someWrongPassword |

  Scenario: Test failure to log in
    _LOGIN_ Given I am logged in with username <username> and password <password>
    _LOGOUT_ I can log out

    Examples:
      | username | password |
      | m.feller@auckland.ac.nz | test123 |

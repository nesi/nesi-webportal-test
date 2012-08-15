Feature: Login

  Scenario: Test logging in
    {LOGIN} Given I go to the login page
    {LOGIN} And set <username> as username
    {LOGIN} And set <password> as password
    {LOGIN} And click the login button
    {LOGIN} Then I am logged in
    {LOGOUT} Log out

    Examples:
      | username | password |
      | m.feller@auckland.ac.nz |  test123 |

  Scenario: Test failure to log in
    {LOGIN} Given I go to the login page
    {LOGIN} And set <username> as username
    {LOGIN} And set <password> as password
    {LOGIN} And click the login button
    {LOGIN} Then I am not logged in

    Examples:
      | username | password |
      | m.feller@auckland.ac.nz | someWrongPassword |

  Scenario: Short version to log in
    {LOGIN} Given I am logged in with username <username> and password <password>
    {LOGOUT} Log out

    Examples:
      | username | password |
      | m.feller@auckland.ac.nz | test123 |

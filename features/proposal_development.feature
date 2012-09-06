Feature: Proposal Development Proposal

  Scenario: Add development proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Proposal Development Class link
    {ADD_PROPOSAL} And the proposal with title <title> does not yet exist
    {ADD_PROPOSAL_DEVELOPMENT} And set title to <title>
    {ADD_PROPOSAL_DEVELOPMENT} And set description to <description>
    {ADD_PROPOSAL_DEVELOPMENT} And set PI name to <piname>
    {ADD_PROPOSAL_DEVELOPMENT} And set PI email to <piemail>
    {ADD_PROPOSAL_DEVELOPMENT} And set PI phone to <piphone>
    {ADD_PROPOSAL_DEVELOPMENT} And set project team member to <member>
    {ADD_PROPOSAL_DEVELOPMENT} And set project team members details to <details>
    {ADD_PROPOSAL_DEVELOPMENT} And set project team hpc experience to <experience>
    {ADD_PROPOSAL_DEVELOPMENT} And set software requirements to <softreq>
    {ADD_PROPOSAL_DEVELOPMENT} And set storage requirements to <storereq>
    {ADD_PROPOSAL_DEVELOPMENT} And click expert support for software installation
    {ADD_PROPOSAL_DEVELOPMENT} And set additional information to <infos>
    {ADD_PROPOSAL_DEVELOPMENT} And click the Save button
    {ADD_PROPOSAL} Then the proposal with title <title> has been created in GOLD and the page contains <confirmation>

    Examples:
      | title         | description | piname | piemail          | piphone | member           | details | experience | softreq | storereq | infos | confirmation     |
      | __ test title | desc        | name   | test@nesi.org.nz | 1234    | test@nesi.org.nz | det     | exp        | soreq   | streq    | in    | has been created |

  Scenario: Error in creating development proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Proposal Development Class link
    {ADD_PROPOSAL} And the proposal with title <title> does not yet exist
    {ADD_PROPOSAL_DEVELOPMENT} And set title to <title>
    {ADD_PROPOSAL_DEVELOPMENT} And set description to <description>
    {ADD_PROPOSAL_DEVELOPMENT} And set PI name to <piname>
    {ADD_PROPOSAL_DEVELOPMENT} And set PI email to <piemail>
    {ADD_PROPOSAL_DEVELOPMENT} And set PI phone to <piphone>
    {ADD_PROPOSAL_DEVELOPMENT} And set project team member to <member>
    {ADD_PROPOSAL_DEVELOPMENT} And set project team members details to <details>
    {ADD_PROPOSAL_DEVELOPMENT} And set project team hpc experience to <experience>
    {ADD_PROPOSAL_DEVELOPMENT} And set software requirements to <softreq>
    {ADD_PROPOSAL_DEVELOPMENT} And set storage requirements to <storereq>
    {ADD_PROPOSAL_DEVELOPMENT} And click expert support for software installation
    {ADD_PROPOSAL_DEVELOPMENT} And set additional information to <infos>
    {ADD_PROPOSAL_DEVELOPMENT} And click the Save button
    {ADD_PROPOSAL} Then the proposal with title <title> has not been created and I see the error message <error>

    Examples:
      | title         | description | piname | piemail          | piphone | member             | details | experience | softreq | storereq | infos | error             |
      | __ test title | desc        |        | test@nesi.org.nz | 1234    | test@nesi.org.nz   | det     | exp        | soreq   | streq    | in    | field is required |

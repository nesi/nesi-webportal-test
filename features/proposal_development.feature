Feature: Proposal Development Proposal

  Scenario: Add development proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Proposal Development link
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
    {ADD_PROPOSAL_DEVELOPMENT} Then the proposal has been created and the page contains <confirmation>

    Examples:
      | title | description | piname | piemail | piphone | member | details | experience | softreq | storereq | infos | confirmation |
      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | has been created |

  Scenario: Error in creating development proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Proposal Development link
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
    {ADD_PROPOSAL} Then I see the error message <error>

    Examples:
      | title | description | piname | piemail | piphone | member | details | experience | softreq | storereq | infos | error |
      | | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Title field is required |

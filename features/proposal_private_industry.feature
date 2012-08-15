Feature: PRIVATE_INDUSTRY Proposal

  Scenario: Add PRIVATE_INDUSTRY proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Private Industry link
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} And set title to <title>
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} And set description to <description>
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} And click the Save button
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} Then the proposal has been created and the page contains <confirmation>

    Examples:
      | title | description | confirmation |
      | test title | test description | has been created |

  Scenario: Error in creating PRIVATE_INDUSTRY proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Private Industry link
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} And set title to <title>
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} And set description to <description>
    {ADD_PROPOSAL_PRIVATE_INDUSTRY} And click the Save button
    {ADD_PROPOSAL} Then I see the error message <error>

    Examples:
      | title | description | error |
      | | test description | Title field is required |
      | test title | | Description field is required |


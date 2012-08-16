Feature: Collaborator Proposal

  Scenario: Add collaborator proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Collaborative link
    {ADD_PROPOSAL_COLLABORATOR} And set title to <title>
    {ADD_PROPOSAL_COLLABORATOR} And set description to <description>
    {ADD_PROPOSAL_COLLABORATOR} And click the Save button
    {ADD_PROPOSAL_COLLABORATOR} Then the proposal has been created and the page contains <confirmation>

    Examples:
      | title | description | confirmation |
      | test title | test description | has been created |

  Scenario: Error in creating collaborator proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Collaborative link
    {ADD_PROPOSAL_COLLABORATOR} And set title to <title>
    {ADD_PROPOSAL_COLLABORATOR} And set description to <description>
    {ADD_PROPOSAL_COLLABORATOR} And click the Save button
    {ADD_PROPOSAL} Then I see the error message <error>

    Examples:
      | title | description | error |
      | | test description | Title field is required |
      | test title | | Description field is required |


Feature: Teaching Proposal

  Scenario: Add teaching proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Teaching link
    {ADD_PROPOSAL} And the proposal with id <title> does not yet exist
    {ADD_PROPOSAL_TEACHING} And set title to <title>
    {ADD_PROPOSAL_TEACHING} And set description to <description>
    {ADD_PROPOSAL_TEACHING} And click the Save button
    {ADD_PROPOSAL} Then the proposal with id <title> has been created in GOLD and the page contains <confirmation>

    Examples:
      | title | description | confirmation |
      | lettuce test title | test description | has been created |

  Scenario: Error in creating teaching proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Teaching link
    {ADD_PROPOSAL} And the proposal with id <title> does not yet exist
    {ADD_PROPOSAL_TEACHING} And set title to <title>
    {ADD_PROPOSAL_TEACHING} And set description to <description>
    {ADD_PROPOSAL_TEACHING} And click the Save button
    {ADD_PROPOSAL} Then the proposal with id <title> has not been created and I see the error message <error>

    Examples:
      | title | description | error |
      | lettuce test title | | Description field is required |


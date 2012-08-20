Feature: Research Proposal

  Scenario: Add Research proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Research link
    {ADD_PROPOSAL} And the proposal with id <title> does not yet exist
    {ADD_PROPOSAL_RESEARCH} And set title to <title>
    {ADD_PROPOSAL_RESEARCH} And set scientific goals to <goals>
    {ADD_PROPOSAL_RESEARCH} And set benefits from hpc to <benefits>
    {ADD_PROPOSAL_RESEARCH} And set allocation profile to <profile>
    {ADD_PROPOSAL_RESEARCH} And click intel cluster as desired hpc platform
    {ADD_PROPOSAL_RESEARCH} And set cpu core hours to <corehours>
    {ADD_PROPOSAL_RESEARCH} And set storage requirements to <storereq>
    {ADD_PROPOSAL_RESEARCH} And set software requirements to <softreq>
    {ADD_PROPOSAL_RESEARCH} And set data transfer to <transfer>
    {ADD_PROPOSAL_RESEARCH} And set PI name to <piname>
    {ADD_PROPOSAL_RESEARCH} And set PI email to <piemail>
    {ADD_PROPOSAL_RESEARCH} And set PI phone to <piphone>
    {ADD_PROPOSAL_RESEARCH} And set project team member to <member>
    {ADD_PROPOSAL_RESEARCH} And set project team members details to <details>
    {ADD_PROPOSAL_RESEARCH} And set background to <background>
    {ADD_PROPOSAL_RESEARCH} And click yes for expert support
    {ADD_PROPOSAL_RESEARCH} And set funding provider to <fundingprovider>
    {ADD_PROPOSAL_RESEARCH} And set funding provider to <fundingamount>
    {ADD_PROPOSAL_RESEARCH} And set further information to <infos>
    {ADD_PROPOSAL_RESEARCH} And click the Save button
    {ADD_PROPOSAL} Then the proposal with id <title> has been created in GOLD and the page contains <confirmation>

    Examples:
      | title | goals | benefits | profile | corehours | storereq | softreq | transfer | piname | piemail | piphone | member | details | background | fundingprovider | fundingamount | infos | confirmation |
      | lettuce test title | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | has been created |

  Scenario: Error in adding Research proposal
    {ADD_PROPOSAL} Given I go to the proposal page
    {ADD_PROPOSAL} And click the Research link
    {ADD_PROPOSAL} And the proposal with id <title> does not yet exist
    {ADD_PROPOSAL_RESEARCH} And set title to <title>
    {ADD_PROPOSAL_RESEARCH} And set scientific goals to <goals>
    {ADD_PROPOSAL_RESEARCH} And set benefits from hpc to <benefits>
    {ADD_PROPOSAL_RESEARCH} And set allocation profile to <profile>
    {ADD_PROPOSAL_RESEARCH} And click intel cluster as desired hpc platform
    {ADD_PROPOSAL_RESEARCH} And set cpu core hours to <corehours>
    {ADD_PROPOSAL_RESEARCH} And set storage requirements to <storereq>
    {ADD_PROPOSAL_RESEARCH} And set software requirements to <softreq>
    {ADD_PROPOSAL_RESEARCH} And set data transfer to <transfer>
    {ADD_PROPOSAL_RESEARCH} And set PI name to <piname>
    {ADD_PROPOSAL_RESEARCH} And set PI email to <piemail>
    {ADD_PROPOSAL_RESEARCH} And set PI phone to <piphone>
    {ADD_PROPOSAL_RESEARCH} And set project team member to <member>
    {ADD_PROPOSAL_RESEARCH} And set project team members details to <details>
    {ADD_PROPOSAL_RESEARCH} And set background to <background>
    {ADD_PROPOSAL_RESEARCH} And click yes for expert support
    {ADD_PROPOSAL_RESEARCH} And set funding provider to <fundingprovider>
    {ADD_PROPOSAL_RESEARCH} And set funding provider to <fundingamount>
    {ADD_PROPOSAL_RESEARCH} And set further information to <infos>
    {ADD_PROPOSAL_RESEARCH} And click the Save button
    {ADD_PROPOSAL} Then the proposal with id <title> has not been created and I see the error message <error>

    Examples:
      | title | goals | benefits | profile | corehours | storereq | softreq | transfer | piname | piemail | piphone | member | details | background | fundingprovider | fundingamount | infos | error |
      | lettuce test title | | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | field is required |

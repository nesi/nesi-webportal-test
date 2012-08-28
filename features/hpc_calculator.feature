Feature: HPC Calculator

  Scenario: Test correct HPC cost calculation for Shared mode
    {HPC_CALC} Given I go to the HPC calculator page
    {HPC_CALC} When I choose platform <platform>
    {HPC_CALC} And set <jobSize> as job size
    {HPC_CALC} And choose Shared mode if available for <platform>
    {HPC_CALC} And set <wallClockHours> as wall clock hours
    {HPC_CALC} And set <jobRuns> as number of job runs
    {HPC_CALC} Then the calculated values are: <cpuCoreHours> <hpcCost> <projectCost> <nesiContribution>

    Examples:
      | platform | jobSize | wallClockHours | jobRuns | cpuCoreHours | hpcCost   | projectCost | nesiContribution |
      | power6   |  32     | 3125           | 1       |  100000      | $20000.00 |  $4000.00   | $16000.00        |
      | power6   |  32     |  625           | 5       |  100000      | $20000.00 |  $4000.00   | $16000.00        |
      | power7   |  32     | 3125           | 1       |  100000      | $20000.00 |  $4000.00   | $16000.00        |
      | power7   |  32     |  625           | 5       |  100000      | $20000.00 |  $4000.00   | $16000.00        |
      | intel    |  12     | 3000           | 1       |   36000      |  $7200.00 |  $1440.00   |  $5760.00        |
      | intel    |  12     | 1500           | 2       |   36000      |  $7200.00 |  $1440.00   |  $5760.00        |
      | bluegene |   1     | 3000           | 1       |  768000      | $38400.00 |  $7680.00   | $30720.00        |
      | bluegene | 256     | 3000           | 1       |  768000      | $38400.00 |  $7680.00   | $30720.00        |
      | bluegene | 257     | 3000           | 1       | 1536000      | $76800.00 | $15360.00   | $61440.00        |
      | bluegene | 257     | 1500           | 2       | 1536000      | $76800.00 | $15360.00   | $61440.00        |

  Scenario: Test error handling for Shared mode
    {HPC_CALC} Given I go to the HPC calculator page
    {HPC_CALC} When I choose platform <platform>
    {HPC_CALC} And set <jobSize> as job size
    {HPC_CALC} And choose Shared mode if available for <platform>
    {HPC_CALC} And set <wallClockHours> as wall clock hours
    {HPC_CALC} And set <jobRuns> as number of job runs
    {HPC_CALC} Then the calculated values are: <cpuCoreHours> <hpcCost> <projectCost> <nesiContribution>
    {HPC_CALC} And I see the following error message on the page: <message>

    Examples:
      | platform | jobSize | wallClockHours | jobRuns | cpuCoreHours | hpcCost | projectCost | nesiContribution | message                         |
      | power6   | -10     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power6   |   a     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power6   |  32     |    a           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power6   |  32     | 3125           | a       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power7   | -10     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power7   |   a     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power7   |  32     |    a           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | power7   |  32     | 3125           | a       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | intel    | -10     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | intel    |   a     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | intel    |  32     |    a           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | intel    |  32     | 3125           | a       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | bluegene | -10     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | bluegene |   a     | 3125           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | bluegene |  32     |    a           | 1       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |
      | bluegene |  32     | 3125           | a       | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted |

  Scenario: Test correct HPC cost calculation for Exclusive mode
    {HPC_CALC} Given I go to the HPC calculator page
    {HPC_CALC} When I choose platform <platform>
    {HPC_CALC} And set <jobSize> as job size
    {HPC_CALC} And choose Exclusive mode
    {HPC_CALC} And set <cpuCoresPerNode> as cpu cores per node
    {HPC_CALC} And set <wallClockHours> as wall clock hours
    {HPC_CALC} And set <jobRuns> as number of job runs
    {HPC_CALC} Then the calculated values are: <cpuCoreHours> <hpcCost> <projectCost> <nesiContribution>
    {HPC_CALC} And the job efficiency is <jobEfficiency>

    Examples:
      | platform | jobSize | cpuCoresPerNode | wallClockHours | jobRuns | jobEfficiency | cpuCoreHours | hpcCost   | projectCost | nesiContribution |
      | power6   | 128     | 10              | 672            | 1       | 31%           | 86016        | $55050.24 | $11010.05   | $44040.19        |
      | power6   | 128     | 10              | 336            | 2       | 31%           | 86016        | $55050.24 | $11010.05   | $44040.19        |
      | power7   | 128     | 10              | 672            | 1       | 31%           | 86016        | $55050.24 | $11010.05   | $44040.19        |
      | power7   | 128     | 10              | 336            | 2       | 31%           | 86016        | $55050.24 | $11010.05   | $44040.19        |
      | intel    | 128     | 10              | 672            | 1       | 83%           | 86016        | $20643.84 |  $4128.77   | $16515.07        |
      | intel    | 128     | 10              | 336            | 2       | 83%           | 86016        | $20643.84 |  $4128.77   | $16515.07        |

  Scenario: Test error handling for Exclusive mode
    {HPC_CALC} Given I go to the HPC calculator page
    {HPC_CALC} When I choose platform <platform>
    {HPC_CALC} And set <jobSize> as job size
    {HPC_CALC} And choose Exclusive mode
    {HPC_CALC} And set <cpuCoresPerNode> as cpu cores per node
    {HPC_CALC} And set <wallClockHours> as wall clock hours
    {HPC_CALC} And set <jobRuns> as number of job runs
    {HPC_CALC} Then the calculated values are: <cpuCoreHours> <hpcCost> <projectCost> <nesiContribution>
    {HPC_CALC} And the job efficiency is <jobEfficiency>
    {HPC_CALC} And I see the following error message on the page: <message>

    Examples:
      | platform | jobSize | cpuCoresPerNode | wallClockHours | jobRuns | jobEfficiency | cpuCoreHours | hpcCost | projectCost | nesiContribution | message                                             |
      | power6   | -10     | 10              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power6   |   a     | 10              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power6   |  32     |  a              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power6   |  10     | 12              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Number of requested CPU cores greater than job size |
      | power6   |  50     | 40              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | No values greater than 32 permitted                 |
      | power6   |  32     | 10              |    a           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power6   |  32     | 10              | 3125           | a       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power7   | -10     | 10              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power7   |   a     | 10              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power7   |  32     |  a              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power7   |  10     | 12              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Number of requested CPU cores greater than job size |
      | power7   |  50     | 40              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | No values greater than 32 permitted                 |
      | power7   |  32     | 10              |    a           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | power7   |  32     | 10              | 3125           | a       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | intel    | -10     | 10              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | intel    |   a     | 10              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | intel    |  32     |  a              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | intel    |  10     | 11              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Number of requested CPU cores greater than job size |
      | intel    |  50     | 40              | 3125           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | No values greater than 12 permitted                 |
      | intel    |  32     | 10              |    a           | 1       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |
      | intel    |  32     | 10              | 3125           | a       | 0%            | 0            | $0.00   | $0.00       | $0.00            | Only positive numbers permitted                     |

  Scenario: Test saving of values when tabs are changed 
    {HPC_CALC} Given I go to the HPC calculator page
    {HPC_CALC} When I choose platform <platform1>
    {HPC_CALC} And set <jobSize1> as job size
    {HPC_CALC} And set <wallClockHours1> as wall clock hours
    {HPC_CALC} When I choose platform <platform2>
    {HPC_CALC} And set <jobSize2> as job size
    {HPC_CALC} And set <wallClockHours2> as wall clock hours
    {HPC_CALC} When I choose platform <platform1>
    {HPC_CALC} Then the values for job size and wall clock hours are: <jobSize1> <wallClockHours1>
    {HPC_CALC} When I choose platform <platform2>
    {HPC_CALC} Then the values for job size and wall clock hours are: <jobSize2> <wallClockHours2>

    Examples:
      | platform1 | jobSize1 | wallClockHours1 | platform2 | jobSize2 | wallClockHours2 |
      | power6    | 42       | 34              | power7    | 56       | 87              |
      | power6    | 42       | 34              | intel     | 56       | 87              |
      | power6    | 42       | 34              | bluegene  | 56       | 87              |

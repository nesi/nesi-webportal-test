Feature: NeSI HPC Calculator

  Scenario: Test correct HPC cost calculation for Shared mode
    Given I go to the NeSI HPC calculator page
    When I choose platform <platform>
    And set <job_size> as job size
    And choose Shared mode if available for <platform>
    And set <wall_clock_hours> as wall clock hours
    And set <job_runs> as number of job runs
    Then the calculated values are: <cpu_core_hours> <hpc_cost> <project_cost> <nesi_contribution>

    Examples:
      | platform | job_size | wall_clock_hours | job_runs | cpu_core_hours | hpc_cost | project_cost | nesi_contribution |
      | power6   |  32      | 3125             | 1        |  100000        | 20000    |  4000        | 16000             |
      | power6   |  32      |  625             | 5        |  100000        | 20000    |  4000        | 16000             |
      | power7   |  32      | 3125             | 1        |  100000        | 20000    |  4000        | 16000             |
      | power7   |  32      |  625             | 5        |  100000        | 20000    |  4000        | 16000             |
      | intel    |  12      | 3000             | 1        |   36000        |  7200    |  1440        |  5760             |
      | intel    |  12      | 1500             | 2        |   36000        |  7200    |  1440        |  5761             |
      | bluegene |  50      | 3000             | 1        |  768000        | 38400    |  7680        | 30720             |
      | bluegene | 255      | 3000             | 1        |  768000        | 38400    |  7680        | 30720             |
      | bluegene | 256      | 3000             | 1        |  768000        | 38400    |  7680        | 30720             |
      | bluegene | 257      | 3000             | 1        | 1536000        | 76800    | 15360        | 61440             |
      | bluegene | 257      | 1500             | 2        | 1536000        | 76800    | 15360        | 61440             |


  Scenario: Test error handling for Shared mode
    Given I go to the NeSI HPC calculator page
    When I choose platform <platform>
    And set <job_s> as job size
    And choose Shared mode if available for <platform>
    And set <wall_clock_h> as wall clock hours
    And set <job_r> as number of job runs
    Then the calculated values are: <cpu_core_h> <hpc_c> <project_c> <nesi_c>
    And I see the following error message on the page: <message>

    Examples:
      | platform | job_s | wall_clock_h | job_r | cpu_core_h | hpc_c | project_c | nesi_c | message                         |
      | power6   | -10   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power6   |   a   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power6   |  32   |    a         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power6   |  32   | 3125         | a     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power7   | -10   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power7   |   a   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power7   |  32   |    a         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | power7   |  32   | 3125         | a     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | intel    | -10   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | intel    |   a   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | intel    |  32   |    a         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | intel    |  32   | 3125         | a     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | bluegene | -10   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | bluegene |   a   | 3125         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | bluegene |  32   |    a         | 1     |  0         | 0     |  0        | 0      | Only positive numbers permitted |
      | bluegene |  32   | 3125         | a     |  0         | 0     |  0        | 0      | Only positive numbers permitted |

  Scenario: Test correct HPC cost calculation for Scaled mode
    Given I go to the NeSI HPC calculator page
    When I choose platform <platform>
    And set <job_size> as job size
    And choose Scaled mode
    And set <cpu_cores_per_node> as cpu cores per node
    And set <wall_clock_hours> as wall clock hours
    And set <job_runs> as number of job runs
    Then the calculated values are: <cpu_core_hours> <hpc_cost> <project_cost> <nesi_contribution>

    Examples:
      | platform | job_size | cpu_cores_per_node | wall_clock_hours | job_runs | cpu_core_hours | hpc_cost | project_cost | nesi_contribution |
      | power6   | 128      | 10                 | 672              | 1        | 86016          | 55050    | 11010        | 44040             |
      | power6   | 128      | 10                 | 336              | 2        | 86016          | 55050    | 11010        | 44040             |
      | power7   | 128      | 10                 | 672              | 1        | 86016          | 55050    | 11010        | 44040             |
      | power7   | 128      | 10                 | 336              | 2        | 86016          | 55050    | 11010        | 44040             |
      | intel    | 128      | 10                 | 672              | 1        | 86016          | 20644    |  4129        | 16515             |
      | intel    | 128      | 10                 | 336              | 2        | 86016          | 20644    |  4129        | 16515             |


  Scenario: Test error handling for Scaled mode
    Given I go to the NeSI HPC calculator page
    When I choose platform <platform>
    And set <job_s> as job size
    And choose Scaled mode
    And set <cpu_c_p_n> as cpu cores per node
    And set <wall_clock_h> as wall clock hours
    And set <job_r> as number of job runs
    Then the calculated values are: <cpu_core_h> <hpc_c> <project_c> <nesi_c>
    And I see the following error message on the page: <message>

    Examples:
      | platform | job_s | cpu_c_p_n | wall_clock_h | job_r | cpu_core_h | hpc_c | project_c | nesi_c | message                                             |
      | power6   | -10   | 10        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power6   |   a   | 10        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power6   |  32   |  a        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power6   |  10   | 12        | 3125         | 1     | 0          | 0     |  0        | 0      | Number of requested CPU cores greater than job size |
      | power6   |  50   | 40        | 3125         | 1     | 0          | 0     |  0        | 0      | No values greater than 32 permitted                 |
      | power6   |  32   | 10        |    a         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power6   |  32   | 10        | 3125         | a     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power7   | -10   | 10        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power7   |   a   | 10        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power7   |  32   |  a        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power7   |  10   | 12        | 3125         | 1     | 0          | 0     |  0        | 0      | Number of requested CPU cores greater than job size |
      | power7   |  50   | 40        | 3125         | 1     | 0          | 0     |  0        | 0      | No values greater than 32 permitted                 |
      | power7   |  32   | 10        |    a         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | power7   |  32   | 10        | 3125         | a     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | intel    | -10   | 10        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | intel    |   a   | 10        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | intel    |  32   |  a        | 3125         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | intel    |  10   | 11        | 3125         | 1     | 0          | 0     |  0        | 0      | Number of requested CPU cores greater than job size |
      | intel    |  50   | 40        | 3125         | 1     | 0          | 0     |  0        | 0      | No values greater than 12 permitted                 |
      | intel    |  32   | 10        |    a         | 1     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |
      | intel    |  32   | 10        | 3125         | a     | 0          | 0     |  0        | 0      | Only positive numbers permitted                     |



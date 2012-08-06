Feature: NeSI HPC Calculator

  Scenario: Test correct HPC cost calculation when job size is a multiple of cpu cores per node
    Given I go to the NeSI HPC calculator page
    When I choose platform <platform>
    And set <job_size> as job size
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
      | intel    |  12      | 1500             | 2        |   36000        |  7200    |  1440        |  5760             |
      | bluegene |  50      | 3000             | 1        |  768000        | 38400    |  7680        | 30720             |
      | bluegene | 255      | 3000             | 1        |  768000        | 38400    |  7680        | 30720             |
      | bluegene | 256      | 3000             | 1        |  768000        | 38400    |  7680        | 30720             |
      | bluegene | 257      | 3000             | 1        | 1536000        | 76800    | 15360        | 61440             |
      | bluegene | 257      | 1500             | 2        | 1536000        | 76800    | 15360        | 61440             |


  Scenario: Test correct HPC cost calculation in Shared mode
    Given I go to the NeSI HPC calculator page
    When I choose platform <platform>
    And set <job_size> as job size
    And choose Shared mode
    And set <wall_clock_hours> as wall clock hours
    And set <job_runs> as number of job runs
    Then the calculated values are: <cpu_core_hours> <hpc_cost> <project_cost> <nesi_contribution>

    Examples:
      | platform | job_size | wall_clock_hours | job_runs | cpu_core_hours | hpc_cost | project_cost | nesi_contribution |
      | power6   |  30      | 3125             | 1        |   93750        | 18750    |  3750        | 15000             |
      | power6   |  30      |  625             | 5        |   93750        | 18750    |  3750        | 15000             |
      | power7   |  30      | 3125             | 1        |   93750        | 18750    |  3750        | 15000             |
      | power7   |  30      |  625             | 5        |   93750        | 18750    |  3750        | 15000             |
      | intel    |  10      | 3000             | 1        |   30000        |  6000    |  1200        |  4800             |
      | intel    |  10      | 1500             | 2        |   30000        |  6000    |  1200        |  4800             |


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

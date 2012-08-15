from time import sleep
from lettuce import world, step

@step('_HPC_CALC_ Given I go to the NeSI HPC calculator page')
def load_hpc_calc_page(step):
  world.browser.get(world.hpc_calc_url)

@step('_HPC_CALC_ When I choose platform (.*)')
def click_tab(step, platform):
  world.hpc_calc_platform = platform
  el = world.browser.find_element_by_xpath("//li[@id='%s_tab']/a[1]" % platform)
  el.click()
  sleep(world.delay)

@step('_HPC_CALC_ And set (.*) as job size')
def set_job_size(step, job_size):
  el = world.browser.find_element_by_id('edit-%s-job-size' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(job_size)
  sleep(world.delay)

@step('_HPC_CALC_ And choose Shared mode if available for (.*)')
def set_mode(step, platform):
  if platform == "bluegene":
    pass
  else:
    radio = world.browser.find_element_by_id('edit-%s-usage-shared' % world.hpc_calc_platform)
    radio.click()
    sleep(world.delay)

@step('_HPC_CALC_ And choose Exclusive mode')
def set_mode(step):
  radio = world.browser.find_element_by_id('edit-%s-usage-exclusive' % world.hpc_calc_platform)
  radio.click()
  sleep(world.delay)
 
@step('_HPC_CALC_ And set (.*) as cpu cores per node')
def set_cpu_cores_per_node(step, cpu_cores_per_node):
  el = world.browser.find_element_by_id('edit-%s-cpu-cores-per-node' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(cpu_cores_per_node)
  sleep(world.delay)
 
@step('_HPC_CALC_ And set (.*) as wall clock hours')
def set_wall_clock_hours(step, wall_clock_hours):
  el = world.browser.find_element_by_id('edit-%s-wall-clock-hours' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(wall_clock_hours)
  sleep(world.delay)

@step('_HPC_CALC_ And set (.*) as number of job runs')
def set_job_runs(step, number_job_runs):
  el = world.browser.find_element_by_id('edit-%s-number-job-runs' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(number_job_runs)
  sleep(world.delay)

@step('_HPC_CALC_ Then the calculated values are: (.*) (.*) (.*) (.*)')
def verify_calculation(step, cpu_core_hours, hpc_cost, project_cost, nesi_contribution):
  assert cpu_core_hours == world.browser.find_element_by_id('edit-%s-cpu-core-hours' % world.hpc_calc_platform).text
  assert hpc_cost == world.browser.find_element_by_id('edit-%s-hpc-cost' % world.hpc_calc_platform).text
  assert project_cost == world.browser.find_element_by_id('edit-%s-project-cost' % world.hpc_calc_platform).text
  assert nesi_contribution == world.browser.find_element_by_id('edit-%s-nesi-contribution' % world.hpc_calc_platform).text
  sleep(world.delay)

@step('_HPC_CALC_ And the job efficiency is (.*)')
def verify_job_efficiency(step, job_efficiency):
  assert job_efficiency == world.browser.find_element_by_id('edit-%s-job-efficiency' % world.hpc_calc_platform).text

@step('_HPC_CALC_ Then the values for job size and wall clock hours are: (.*) (.*)')
def verify_jobsize_and_cpu_cores_per_node(step, job_size, wall_clock_hours):
  assert job_size == world.browser.find_element_by_id('edit-%s-job-size' % world.hpc_calc_platform).get_attribute("value")
  assert wall_clock_hours == world.browser.find_element_by_id('edit-%s-wall-clock-hours' % world.hpc_calc_platform).get_attribute("value")
  
@step('_HPC_CALC_ And I see the following error message on the page: (.*)')
def check_error_message_on_page(step, message):
  assert message in world.browser.page_source
   

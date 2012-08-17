# steps for the hpc calculator

from lettuce import world, step
from selenium.webdriver.support.ui import WebDriverWait as WebDriverWait

@step('{HPC_CALC} Given I go to the HPC calculator page')
def HPC_CALC_load_hpc_calc_page(step):
  world.browser.get(world.hpc_calc_url)

@step('{HPC_CALC} When I choose platform (.*)')
def HPC_CALC_click_tab(step, platform):
  world.hpc_calc_platform = platform
  el = world.browser.find_element_by_xpath("//li[@id='%s_tab']/a[1]" % platform)
  el.click()

@step('{HPC_CALC} And set (.*) as job size')
def HPC_CALC_set_job_size(step, job_size):
  el = world.browser.find_element_by_id('edit-%s-job-size' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(job_size)

@step('{HPC_CALC} And choose Shared mode if available for (.*)')
def HPC_CALC_set_shared_mode(step, platform):
  if platform == "bluegene":
    pass
  else:
    radio = world.browser.find_element_by_id('edit-%s-usage-shared' % world.hpc_calc_platform)
    radio.click()

@step('{HPC_CALC} And choose Exclusive mode')
def HPC_CALC_set_exclusive_mode(step):
  radio = world.browser.find_element_by_id('edit-%s-usage-exclusive' % world.hpc_calc_platform)
  radio.click()
 
@step('{HPC_CALC} And set (.*) as cpu cores per node')
def HPC_CALC_set_cpu_cores_per_node(step, cpu_cores_per_node):
  el = world.browser.find_element_by_id('edit-%s-cpu-cores-per-node' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(cpu_cores_per_node)
 
@step('{HPC_CALC} And set (.*) as wall clock hours')
def HPC_CALC_set_wall_clock_hours(step, wall_clock_hours):
  el = world.browser.find_element_by_id('edit-%s-wall-clock-hours' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(wall_clock_hours)

@step('{HPC_CALC} And set (.*) as number of job runs')
def HPC_CALC_set_job_runs(step, number_job_runs):
  el = world.browser.find_element_by_id('edit-%s-number-job-runs' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(number_job_runs)

@step('{HPC_CALC} Then the calculated values are: (.*) (.*) (.*) (.*)')
def HPC_CALC_verify_calculation(step, cpu_core_hours, hpc_cost, project_cost, nesi_contribution):
  assert cpu_core_hours == world.browser.find_element_by_id('edit-%s-cpu-core-hours' % world.hpc_calc_platform).text
  assert hpc_cost == world.browser.find_element_by_id('edit-%s-hpc-cost' % world.hpc_calc_platform).text
  assert project_cost == world.browser.find_element_by_id('edit-%s-project-cost' % world.hpc_calc_platform).text
  assert nesi_contribution == world.browser.find_element_by_id('edit-%s-nesi-contribution' % world.hpc_calc_platform).text

@step('{HPC_CALC} And the job efficiency is (.*)')
def HPC_CALC_verify_job_efficiency(step, job_efficiency):
  assert job_efficiency == world.browser.find_element_by_id('edit-%s-job-efficiency' % world.hpc_calc_platform).text

@step('{HPC_CALC} Then the values for job size and wall clock hours are: (.*) (.*)')
def HPC_CALC_verify_jobsize_and_cpu_cores_per_node(step, job_size, wall_clock_hours):
  assert job_size == world.browser.find_element_by_id('edit-%s-job-size' % world.hpc_calc_platform).get_attribute("value")
  assert wall_clock_hours == world.browser.find_element_by_id('edit-%s-wall-clock-hours' % world.hpc_calc_platform).get_attribute("value")
  
@step('{HPC_CALC} And I see the following error message on the page: (.*)')
def HPC_CALC_check_error_message_on_page(step, message):
  wait = WebDriverWait(world.browser, world.timeout)
  wait.until(lambda d: message in world.browser.page_source)

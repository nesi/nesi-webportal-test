from time import sleep
from lettuce import world, step

@step('Given I go to the NeSI HPC calculator page')
def load_hpc_calc_page(step):
  world.browser.get(world.hpc_calc_url)

@step('When I choose platform (.*)')
def click_tab(step, platform):
  world.hpc_calc_platform = platform
  el = world.browser.find_element_by_xpath("//li[@id='%s_tab']/a[1]" % platform)
  el.click()
  sleep(world.delay)

@step('And set (.*) as job size')
def set_job_size(step, job_size):
  el = world.browser.find_element_by_id('edit-%s-job-size' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(job_size)
  sleep(world.delay)

@step('And choose Shared mode if available for (.*)')
def set_mode(step, platform):
  if platform == "bluegene":
    pass
  else:
    radio = world.browser.find_element_by_id('edit-%s-usage-shared' % world.hpc_calc_platform)
    radio.click()
    sleep(world.delay)

@step('And choose Scaled mode')
def set_mode(step):
  radio = world.browser.find_element_by_id('edit-%s-usage-scaled' % world.hpc_calc_platform)
  radio.click()
  sleep(world.delay)
 
@step('And set (.*) as cpu cores per node')
def set_cpu_cores_per_node(step, cpu_cores_per_node):
  el = world.browser.find_element_by_id('edit-%s-cpu-cores' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(cpu_cores_per_node)
  sleep(world.delay)
 
@step('And set (.*) as wall clock hours')
def set_wall_clock_hours(step, wall_clock_hours):
  el = world.browser.find_element_by_id('edit-%s-wall-clock-hours' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(wall_clock_hours)
  sleep(world.delay)

@step('And set (.*) as number of job runs')
def set_job_runs(step, number_job_runs):
  el = world.browser.find_element_by_id('edit-%s-number-job-runs' % world.hpc_calc_platform)
  el.clear()
  el.send_keys(number_job_runs)
  sleep(world.delay)

@step('the calculated values are: (.*) (.*) (.*) (.*)')
def verify_calculation(step, cpu_core_hours, hpc_cost, project_cost, nesi_contrib):
  assert cpu_core_hours == world.browser.find_element_by_id('edit-%s-core-cpu-hours-value' % world.hpc_calc_platform).text
  assert hpc_cost == world.browser.find_element_by_id('edit-%s-hpc-cost-value' % world.hpc_calc_platform).text
  assert project_cost == world.browser.find_element_by_id('edit-%s-project-cost-value' % world.hpc_calc_platform).text
  assert nesi_contrib == world.browser.find_element_by_id('edit-%s-nesi-contrib-value' % world.hpc_calc_platform).text
  sleep(world.delay)

@step('And I see the following error message on the page: (.*)')
def check_error_message_on_page(step, message):
  assert message in world.browser.page_source
   


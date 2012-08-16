# steps for research proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL_RESEARCH} And set title to (.*)')
def ADD_PROPOSAL_RESEARCH_set_title(step, val):
  el = world.browser.find_element_by_id('edit-title')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set scientific goals to (.*)')
def ADD_PROPOSAL_RESEARCH_set_scientific_goals(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-scientific-goals-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set benefits from hpc to (.*)')
def ADD_PROPOSAL_RESEARCH_set_benefits_from_hpc(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-hpc-benefits-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set allocation profile to (.*)')
def ADD_PROPOSAL_RESEARCH_set_allocation_profile(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-allocation-profile-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click intel cluster as desired hpc platform')
def ADD_PROPOSAL_RESEARCH_click_intel_cluster(step):
  el = world.browser.find_element_by_id('edit-field-prc-proposed-hpc-platform-und-intel-cluster')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click power6 as desired hpc platform')
def ADD_PROPOSAL_RESEARCH_click_power6(step):
  el = world.browser.find_element_by_id('edit-field-prc-proposed-hpc-platform-und-power6')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click power7 as desired hpc platform')
def ADD_PROPOSAL_RESEARCH_click_power7(step):
  el = world.browser.find_element_by_id('edit-field-prc-proposed-hpc-platform-und-power7')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click bluegene as desired hpc platform')
def ADD_PROPOSAL_RESEARCH_click_bluegene(step):
  el = world.browser.find_element_by_id('edit-field-prc-proposed-hpc-platform-und-bluegene')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click unknown as desired hpc platform')
def ADD_PROPOSAL_RESEARCH_click_unknown(step):
  el = world.browser.find_element_by_id('edit-field-prc-proposed-hpc-platform-und-unknown')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set cpu core hours to (.*)')
def ADD_PROPOSAL_RESEARCH_set_cpu_core_hours(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-cpu-core-hours-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set storage requirements to (.*)')
def ADD_PROPOSAL_RESEARCH_set_storage_requirements(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-storage-requirements-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set software requirements to (.*)')
def ADD_PROPOSAL_RESEARCH_set_software_requirements(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-software-requirements-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set data transfer to (.*)')
def ADD_PROPOSAL_RESEARCH_set_data_transfer(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-data-transfer-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set PI name to (.*)')
def ADD_PROPOSAL_RESEARCH_set_pi_name(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-pi-name-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set PI email to (.*)')
def ADD_PROPOSAL_RESEARCH_set_pi_email(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-pi-email-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set PI phone to (.*)')
def ADD_PROPOSAL_RESEARCH_set_pi_phone(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-pi-phone-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set project team member to (.*)')
def ADD_PROPOSAL_RESEARCH_set_project_team_member(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-team-member-emails-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set project team members details to (.*)')
def ADD_PROPOSAL_RESEARCH_set_project_team_members_details(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-team-members-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set background to (.*)')
def ADD_PROPOSAL_RESEARCH_set_background(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-hpc-background-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click yes for expert support')
def ADD_PROPOSAL_RESEARCH_click_yes_for_expert_support(step):
  el = world.browser.find_element_by_id('edit-field-prc-expert-support-und-yes')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click no for expert support')
def ADD_PROPOSAL_RESEARCH_click_no_for_expert_support(step):
  el = world.browser.find_element_by_id('edit-field-prc-expert-support-und-no')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set funding provider to (.*)')
def ADD_PROPOSAL_RESEARCH_set_funding_provider(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-funding-provider-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set funding amount to (.*)')
def ADD_PROPOSAL_RESEARCH_set_funding_amount(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-funding-amount-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And set further information to (.*)')
def ADD_PROPOSAL_RESEARCH_set_additional_information(step, val):
  el = world.browser.find_element_by_id('edit-field-prc-additional-information-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} And click the Save button')
def ADD_PROPOSAL_RESEARCH_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_RESEARCH} Then the proposal has been created and the page contains (.*)')
def ADD_PROPOSAL_RESEARCH_verify_creation(step, confirmation):
  sleep(world.delay)
  assert confirmation in world.browser.page_source

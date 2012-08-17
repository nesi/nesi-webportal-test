# steps for development proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL_DEVELOPMENT} And set title to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_title(step, val):
  try:
    el = world.browser.find_element_by_id('edit-title')
    el.clear()
    el.send_keys(val)
    sleep(world.delay)
  except:
    world.browser.save_screenshot('/tmp/screenie.png')
    assert False

@step('{ADD_PROPOSAL_DEVELOPMENT} And set description to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_description(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-description-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set PI name to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_pi_name(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-pi-name-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set PI email to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_pi_email(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-pi-email-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set PI phone to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_pi_phone(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-pi-phone-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set project team member to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_project_team_member(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-team-member-emails-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set project team members details to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_project_team_members_details(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-team-members-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set project team hpc experience to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_project_team_hpceperience(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-team-hpcexperience-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set software requirements to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_software_requirements(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-software-requirements-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set storage requirements to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_storage_requirements(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-storage-requirements-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And click expert support for software installation')
def ADD_PROPOSAL_DEVELOPMENT_set_support_for_software_installation(step):
  el = world.browser.find_element_by_id('edit-field-pdc-expert-support-und-software-installation')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And click expert support for software porting')
def ADD_PROPOSAL_DEVELOPMENT_set_support_for_software_porting(step):
  el = world.browser.find_element_by_id('edit-field-pdc-expert-support-und-software-porting')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And click expert support for software optimisation')
def ADD_PROPOSAL_DEVELOPMENT_set_support_for_software_optimisation(step):
  el = world.browser.find_element_by_id('edit-field-pdc-expert-support-und-software-optimisation')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And click expert support for scaling performance')
def ADD_PROPOSAL_DEVELOPMENT_set_support_for_scaling_performance(step):
  el = world.browser.find_element_by_id('edit-field-pdc-expert-support-und-scaling-performance')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And set additional information to (.*)')
def ADD_PROPOSAL_DEVELOPMENT_set_additional_information(step, val):
  el = world.browser.find_element_by_id('edit-field-pdc-additional-information-und-0-value')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} And click the Save button')
def ADD_PROPOSAL_DEVELOPMENT_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_DEVELOPMENT} Then the proposal has been created and the page contains (.*)')
def ADD_PROPOSAL_DEVELOPMENT_verify_creation(step, confirmation):
  try:
    assert confirmation in world.browser.page_source
  except:
    world.browser.save_screenshot('/tmp/screenie.png')
    assert False

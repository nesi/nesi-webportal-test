# steps for COLLABORATOR proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL_COLLABORATOR} And set title to (.*)')
def ADD_PROPOSAL_COLLABORATOR_set_title(step, val):
  try:
    el = world.browser.find_element_by_id('edit-title')
    el.clear()
    el.send_keys(val)
    sleep(world.delay)
  except:
    world.browser.save_screenshot('/tmp/screenie.png')

@step('{ADD_PROPOSAL_COLLABORATOR} And set description to (.*)')
def ADD_PROPOSAL_COLLABORATOR_set_description(step, description):
  el = world.browser.find_element_by_id('edit-field-pc-description-und-0-value')
  el.clear()
  el.send_keys(description)
  sleep(world.delay)

@step('{ADD_PROPOSAL_COLLABORATOR} And click the Save button')
def ADD_PROPOSAL_COLLABORATOR_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_COLLABORATOR} Then the proposal has been created and the page contains (.*)')
def ADD_PROPOSAL_COLLABORATOR_verify_creation(step, confirmation):
  assert confirmation in world.browser.page_source

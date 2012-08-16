# steps for collaborative proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL_COLLABORATIVE} And set title to (.*)')
def ADD_PROPOSAL_COLLABORATIVE_set_title(step, title):
  el = world.browser.find_element_by_id('edit-title')
  el.clear()
  el.send_keys(title)
  sleep(world.delay)

@step('{ADD_PROPOSAL_COLLABORATIVE} And set description to (.*)')
def ADD_PROPOSAL_COLLABORATIVE_set_description(step, description):
  el = world.browser.find_element_by_id('edit-field-pc-description-und-0-value')
  el.clear()
  el.send_keys(description)
  sleep(world.delay)

@step('{ADD_PROPOSAL_COLLABORATIVE} And click the Save button')
def ADD_PROPOSAL_COLLABORATIVE_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_COLLABORATIVE} Then the proposal has been created and the page contains (.*)')
def ADD_PROPOSAL_COLLABORATIVE_verify_creation(step, confirmation):
  assert confirmation in world.browser.page_source

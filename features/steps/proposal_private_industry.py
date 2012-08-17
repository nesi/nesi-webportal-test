# steps for private industry proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} And set title to (.*)')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_set_title(step, val):
  try:
    el = world.browser.find_element_by_id('edit-title')
    el.clear()
    el.send_keys(val)
    sleep(world.delay)
  except:
    world.browser.save_screenshot('error_screenshot.png')
    raise

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} And set description to (.*)')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_set_description(step, description):
  el = world.browser.find_element_by_id('edit-field-ppi-description-und-0-value')
  el.clear()
  el.send_keys(description)
  sleep(world.delay)

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} And click the Save button')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} Then the proposal has been created and the page contains (.*)')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_verify_creation(step, confirmation):
  try:
    assert confirmation in world.browser.page_source
  except:
    world.browser.save_screenshot('error_screenshot.png')
    raise

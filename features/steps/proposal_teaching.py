# steps for teaching proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL_TEACHING} And set title to (.*)')
def ADD_PROPOSAL_TEACHING_set_title(step, val):
  el = world.browser.find_element_by_id('edit-title')
  el.clear()
  el.send_keys(val)
  sleep(world.delay)

@step('{ADD_PROPOSAL_TEACHING} And set description to (.*)')
def ADD_PROPOSAL_TEACHING_set_description(step, description):
  el = world.browser.find_element_by_id('edit-field-ptch-description-und-0-value')
  el.clear()
  el.send_keys(description)
  sleep(world.delay)

@step('{ADD_PROPOSAL_TEACHING} And click the Save button')
def ADD_PROPOSAL_TEACHING_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()
  sleep(world.delay)

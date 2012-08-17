# steps for COLLABORATOR proposal creation

from lettuce import world, step

@step('{ADD_PROPOSAL_COLLABORATOR} And set title to (.*)')
def ADD_PROPOSAL_COLLABORATOR_set_title(step, val):
  el = world.browser.find_element_by_id('edit-title')
  el.clear()
  el.send_keys(val)

@step('{ADD_PROPOSAL_COLLABORATOR} And set description to (.*)')
def ADD_PROPOSAL_COLLABORATOR_set_description(step, description):
  el = world.browser.find_element_by_id('edit-field-pc-description-und-0-value')
  el.clear()
  el.send_keys(description)

@step('{ADD_PROPOSAL_COLLABORATOR} And click the Save button')
def ADD_PROPOSAL_COLLABORATOR_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()

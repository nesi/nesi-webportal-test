# steps for private industry proposal creation

from lettuce import world, step

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} And set title to (.*)')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_set_title(step, val):
  el = world.browser.find_element_by_id('edit-title')
  el.clear()
  el.send_keys(val)

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} And set description to (.*)')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_set_description(step, description):
  el = world.browser.find_element_by_id('edit-field-ppi-description-und-0-value')
  el.clear()
  el.send_keys(description)

@step('{ADD_PROPOSAL_PRIVATE_INDUSTRY} And click the Save button')
def ADD_PROPOSAL_PRIVATE_INDUSTRY_save(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()

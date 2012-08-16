# steps for proposal creation

from time import sleep
from lettuce import world, step

@step('{ADD_PROPOSAL} Given I go to the proposal page')
def ADD_PROPOSAL_load_proposal_page(step):
  world.browser.get(world.add_proposal_url)

@step('{ADD_PROPOSAL} Then I see the error message (.*)')
def ADD_PROPOSAL_verify_error(step, error):
  assert error in world.browser.page_source

@step('{ADD_PROPOSAL} And click the Teaching link')
def ADD_PROPOSAL_click_teaching(step):
  el = world.browser.find_element_by_link_text('Teaching')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL} And click the Private Industry link')
def ADD_PROPOSAL_click_private_industry(step):
  el = world.browser.find_element_by_link_text('Private Industry')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL} And click the Collaborative link')
def ADD_PROPOSAL_click_collaborative(step):
  el = world.browser.find_element_by_link_text('Collaborative')
  el.click()
  sleep(world.delay)

@step('{ADD_PROPOSAL} And click the Proposal Development link')
def ADD_PROPOSAL_click_proposal_development(step):
  el = world.browser.find_element_by_link_text('Proposal Development')
  el.click()
  sleep(world.delay)

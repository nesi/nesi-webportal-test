# steps for proposal creation

from lettuce import world, step
import util

@step('{ADD_PROPOSAL} Given I go to the proposal page')
def ADD_PROPOSAL_load_proposal_page(step):
  world.browser.get(world.add_proposal_url)

@step('{ADD_PROPOSAL} Then the proposal with id (.*) has been created in GOLD and the page contains (.*)')
def ADD_PROPOSAL_verify_creation(step, project_id, confirmation):
  util.find_on_page(confirmation)
  world.goldwrap.get_project(project_id)
  world.goldwrap.delete_project(project_id)
  
@step('{ADD_PROPOSAL} And the proposal with id (.*) does not yet exist')
def ADD_PROPOSAL_verify_absence(step, project_id):
  try:
    world.goldwrap.get_project(project_id)
  except:
    return
  raise Exception('Project with id \'%s\' already exists' % project_id)
  
@step('{ADD_PROPOSAL} Then the proposal with id (.*) has not been created and I see the error message (.*)')
def ADD_PROPOSAL_verify_error(step, project_id, error):
  util.find_on_page(error)
  try:
    world.goldwrap.get_project(project_id)
  except:
    return
  raise Exception('Project with id \'%s\' should not have been created' % project_id)

@step('{ADD_PROPOSAL} And click the Teaching link')
def ADD_PROPOSAL_click_teaching(step):
  el = world.browser.find_element_by_link_text('Teaching')
  el.click()

@step('{ADD_PROPOSAL} And click the Private Industry link')
def ADD_PROPOSAL_click_private_industry(step):
  el = world.browser.find_element_by_link_text('Private Industry')
  el.click()

@step('{ADD_PROPOSAL} And click the Collaborative link')
def ADD_PROPOSAL_click_collaborative(step):
  el = world.browser.find_element_by_link_text('Collaborative')
  el.click()

@step('{ADD_PROPOSAL} And click the Proposal Development link')
def ADD_PROPOSAL_click_proposal_development(step):
  el = world.browser.find_element_by_link_text('Proposal Development')
  el.click()

@step('{ADD_PROPOSAL} And click the Research link')
def ADD_PROPOSAL_click_research_development(step):
  el = world.browser.find_element_by_link_text('Research')
  el.click()

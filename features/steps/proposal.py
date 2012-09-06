# steps for proposal creation

from lettuce import world, step
import util

@step('{ADD_PROPOSAL} Given I go to the proposal page')
def ADD_PROPOSAL_load_proposal_page(step):
  world.browser.get(world.add_proposal_url)

@step('{ADD_PROPOSAL} Then the proposal with title (.*) has been created in GOLD and the page contains (.*)')
def ADD_PROPOSAL_verify_creation(step, project_title, confirmation):
  world.goldwrap.get_project_by_title(project_title)
  world.goldwrap.delete_project_by_title(project_title)
  util.find_on_page(confirmation)
  
@step('{ADD_PROPOSAL} And the proposal with title (.*) does not yet exist')
def ADD_PROPOSAL_verify_absence(step, project_title):
  try:
    world.goldwrap.get_project_by_title(project_title)
  except:
    return
  raise Exception('Project with id \'%s\' already exists' % project_title)
  
@step('{ADD_PROPOSAL} Then the proposal with title (.*) has not been created and I see the error message (.*)')
def ADD_PROPOSAL_verify_error(step, project_title, error):
  util.find_on_page(error)
  try:
    world.goldwrap.get_project_by_title(project_title)
  except:
    return
  raise Exception('Project with id \'%s\' should not have been created' % project_title)

@step('{ADD_PROPOSAL} And click the Teaching link')
def ADD_PROPOSAL_click_teaching(step):
  el = world.browser.find_element_by_link_text('Teaching')
  el.click()

@step('{ADD_PROPOSAL} And click the Private Industry link')
def ADD_PROPOSAL_click_private_industry(step):
  el = world.browser.find_element_by_link_text('Private Industry')
  el.click()

@step('{ADD_PROPOSAL} And click the Collaborator link')
def ADD_PROPOSAL_click_collaborative(step):
  el = world.browser.find_element_by_link_text('Collaborator')
  el.click()

@step('{ADD_PROPOSAL} And click the Proposal Development Class link')
def ADD_PROPOSAL_click_proposal_development(step):
  el = world.browser.find_element_by_link_text('Proposal Development Class')
  el.click()

@step('{ADD_PROPOSAL} And click the Proposal Research Class link')
def ADD_PROPOSAL_click_research_development(step):
  el = world.browser.find_element_by_link_text('Proposal Research Class')
  el.click()

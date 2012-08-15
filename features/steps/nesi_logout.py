from time import sleep
from lettuce import world, step

@step('_LOGOUT_ I can log out')
def LOGOUT_logout(step):
  el = world.browser.find_element_by_link_text('Log out')
  el.click()
  sleep(world.delay)


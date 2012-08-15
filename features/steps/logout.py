# steps for logging out

from time import sleep
from lettuce import world, step

@step('{LOGOUT} Log out')
def LOGOUT_logout(step):
  world.browser.get(world.base_url)
  el = world.browser.find_element_by_link_text('Log out')
  el.click()
  sleep(world.delay)


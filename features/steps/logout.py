# steps for logging out

from time import sleep
from lettuce import world, step

@step('{LOGOUT} Log out')
def LOGOUT_logout(step):
  world.browser.get(world.logout_url)
  sleep(world.delay)


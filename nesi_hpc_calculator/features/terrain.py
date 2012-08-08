from selenium import webdriver
from lettuce import world, before, after

#URL = 'https://web.dev.nesi.org.nz/hpc-calc'
URL = 'http://cluster.ceres.auckland.ac.nz/drupal/hpc-calc'
BROWSER = 'webdriver.Firefox()'
HEADLESS = True
DELAY = 0

@before.all
def setup_browser():
    if HEADLESS:
      from pyvirtualdisplay import Display
      world.display = Display(visible=0, size=(800, 600))
      world.display.start()

    world.browser = eval(BROWSER)
    world.hpc_calc_url = URL
    world.delay = DELAY

@after.all
def shutdown_browser(total):
    world.browser.quit()
    if HEADLESS:
      world.display.stop()

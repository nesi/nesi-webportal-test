from selenium import webdriver
from lettuce import world, before, after

LOGIN_URL = 'https://web.dev.nesi.org.nz/user'
REGISTER_URL = 'https://web.dev.nesi.org.nz/user/register'
HPC_CALC_URL = 'https://web.dev.nesi.org.nz/hpc-calc'
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
    world.login_url = LOGIN_URL
    world.register_url = REGISTER_URL
    world.hpc_calc_url = HPC_CALC_URL
    world.delay = DELAY

@after.all
def shutdown_browser(total):
    world.browser.quit()
    if HEADLESS:
      world.display.stop()

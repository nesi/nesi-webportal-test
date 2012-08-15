from selenium import webdriver
from lettuce import world, before, after
from steps import login, logout

# configuration parameters
USER = 'm.feller@auckland.ac.nz'
PASSWORD = 'test123'
BASE_URL = 'https://web.dev.nesi.org.nz'
LOGIN_PATH = '/user'
REGISTER_PATH = '/user/register'
HPC_CALC_PATH = '/hpc-calc'
ADD_PROPOSAL_PATH = '/add-proposal'
BROWSER = 'webdriver.Firefox()'
HEADLESS = True
DELAY = 0

@before.all
def setup_browser():
    '''
    set up virtual display, set global variables, log in
    '''
    if HEADLESS:
      from pyvirtualdisplay import Display
      world.display = Display(visible=0, size=(800, 600))
      world.display.start()

    world.browser = eval(BROWSER)
    world.base_url = BASE_URL
    world.login_url = BASE_URL + LOGIN_PATH
    world.register_url = BASE_URL + REGISTER_PATH
    world.hpc_calc_url = BASE_URL + HPC_CALC_PATH
    world.add_proposal_url = BASE_URL + ADD_PROPOSAL_PATH
    world.delay = DELAY
    
    login.LOGIN_log_in(step='', user=USER, password=PASSWORD)


@after.all
def shutdown_browser(total):
    '''
      log out, terminate browser and stop virtual display
    '''
    logout.LOGOUT_logout(step='')
    world.browser.quit()
    if HEADLESS:
      world.display.stop()

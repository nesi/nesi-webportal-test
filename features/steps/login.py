# steps for logging in

from lettuce import world, step
from selenium.webdriver.support.ui import WebDriverWait as WebDriverWait

@step('{LOGIN} Given I go to the login page')
def LOGIN_load_login_page(step):
  world.browser.get(world.login_url)

@step('{LOGIN} And set (.*) as username')
def LOGIN_set_username(step, username):
  el = world.browser.find_element_by_id('edit-name')
  el.clear()
  el.send_keys(username)

@step('{LOGIN} And set (.*) as password')
def LOGIN_set_password(step, password):
  el = world.browser.find_element_by_id('edit-pass')
  el.clear()
  el.send_keys(password)

@step('{LOGIN} And click the login button')
def LOGIN_click_login_button(step):
  el = world.browser.find_element_by_id('edit-submit')
  el.click()

@step('{LOGIN} Then I am logged in')
def LOGIN_check_logged_in(step):
  wait = WebDriverWait(world.browser, world.timeout)
  wait.until(lambda d: 'Log out' in world.browser.page_source)

@step('{LOGIN} Then I am not logged in')
def LOGIN_check_not_logged_in(step):
  wait = WebDriverWait(world.browser, world.timeout)
  wait.until(lambda d: 'Sorry, unrecognized username or password.' in world.browser.page_source)

@step('{LOGIN} Given I am logged in with user (.*) and password (.*)')
def LOGIN_log_in(step, user, password):
  LOGIN_load_login_page(step)
  LOGIN_set_username(step, user)
  LOGIN_set_password(step, password)
  LOGIN_click_login_button(step)
  LOGIN_check_logged_in(step)

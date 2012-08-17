from selenium.webdriver.support.ui import WebDriverWait as WebDriverWait
from lettuce import world

def find_on_page(text):
  wait = WebDriverWait(world.browser, world.timeout)
  wait.until(lambda d: text in world.browser.page_source)

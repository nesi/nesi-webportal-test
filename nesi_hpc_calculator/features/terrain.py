from selenium import webdriver
from lettuce import world, before, after

@before.all
def setup_browser():
    world.browser = webdriver.Firefox()
    world.hpc_calc_url = "https://web.dev.nesi.org.nz/hpc-calc"
    world.delay = 0

@after.all
def shutdown_browser(total):
    world.browser.quit()


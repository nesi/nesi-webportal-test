Tests for the NeSI web portal
=============================

The tests are based on Selenium and lettuce (Python tool for Behavior Driven Development (BDD))

Prerequisites
-------------
* Python v2.6, v2.7

For installing the dependencies: pip

Install package dependencies
----------------------------
pip install -r requirements.pip

Configure tests
---------------
Edit features/terrain.py to configure
* USER: User registered with the portal, who can log in
* PASSWORD: Password of the user
* BASE_URL: Base portal URL
* GOLDWRAP_PROTOCOL: protocol (http, https)
* GOLDWRAP_HOST: Name of the machine where goldwrap runs
* GOLDWRAP_PORT: Port at which goldwrap listens
* GOLDWRAP_BASE_PATH: Path where goldwrap is available
* LOGIN_PATH: Path of the login page
* ADD_PROPOSAL_PATH: Path of the page to create proposals
* HPC_CALC_PATH: Path of the HPC calculator page
* BROWSER: Browser to be used (default: webdriver.Firefox())
* HEADLESS: If set to true the Browser is run in headless mode (default: False). TODO: describe dependencies
* TIMEOUT: Max time to wait for text to appear on page or to find div elements on page (default: 60[s])

Run tests
---------
Run 'lettuce' in the top-level folder to run all features.
To run an individual feature, e.g. the login feature: 'lettuce features/nesi_login.feature'
To run the first scenario of a feature, e.g. the login feature: 'lettuce features/nesi_login.feature 1'

Note: The command 'lettuce' is available after the dependencies are installed.

Understand what is tested and how to add test cases
---------------------------------------------------
The tests are defined in features/*.feature in the Gherkin language.
As such they should be pretty straight-forward to read, and it should be relatively easy to add
new test cases for the given scenarios by adding rows to the 'Examples' table of a scenario.



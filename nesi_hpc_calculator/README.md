Tests for the NeSI HPC calculator
=================================

The tests are based on Selenium and lettuce (Python tool for Behavior Driven Development (BDD))

Prerequisites
-------------
* Python 2.7

Python 2.6 will probably work too, but I didn't test it.
For installing the dependencies: pip

Install package dependencies
----------------------------
pip install -r requirements.pip

Configure tests
---------------
Edit features/terrain.py to configure
* URL of the HPC calculator (default: https://web.dev.nesi.org.nz/hpc-calc)
* BROWSER: Browser to be used (default: webdriver.Firefox())
* HEADLESS: If set to true the Browser is run in headless mode (default: False). TODO: describe dependencies
* DELAY: For things to run slower in the browser (default: 0)

Run tests
---------
Run 'lettuce' in the top-level folder of this module (nesi_hpc_calculator).
Note: The command 'lettuce' is available after the dependencies are installed.

Understand what is tested and how to add test cases
---------------------------------------------------
The tests are defined in features/nesi_hpc_calculator.feature in the Gherkin language.
As such they should be pretty straight-forward to read, and it should be relatively easy to add
new test cases for the given scenarios by adding rows to the 'Examples' table of a scenario.



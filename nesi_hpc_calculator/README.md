Tests for the NeSI HPC calculator
=================================

The tests are based on Selenium and lettuce (Python tool for Behavior Driven Development(BDD))

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
Edit features/terrain.py to
* Configure the URL to the HPC calculator in the variable world.hpc_calc_url.
* Configure the browser in the variable world.browser. Currently, Firefox is used.

Run tests
---------
Run 'lettuce' (command is available after installing the dependencies) in the top-level folder.

Understand what is tested and how to add test cases
---------------------------------------------------
The tests are defined in features/nesi_hpc_calculator.feature in the Gherkin language.
As such they should be pretty straight-forward to read, and it should be relatively easy to add
new test cases for the given scenarios by adding rows to the 'Examples' table of a scenario.



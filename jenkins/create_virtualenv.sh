#!/usr/bin/env bash

echo "############################ Create virtualenv ############################"
venv="/tmp/__tmp-nesi-webportal-test-virtualenv"
rm -rf ${venv}
virtualenv ${venv}
source ${venv}/bin/activate
pip install -r requirements.pip > /dev/null
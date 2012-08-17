#!/usr/bin/env bash

set -e

venv="/tmp/__tmp-nesi-webportal-test-virtualenv"
lettuce_output="/tmp/__tmp-nesi-webportal-test.out"

trap "rm -rf ${venv}; rm -f ${lettuce_output}" INT TERM EXIT

echo "############################ Create virtualenv ############################"
rm -rf ${venv}
virtualenv ${venv}
source ${venv}/bin/activate
pip install -r requirements.pip > /dev/null

echo "############################ Run selenium/lettuce tests ############################"
source ${venv}/bin/activate
lettuce > ${lettuce_output}
# purpose of call to sed: remove colors from lettuce output
cat ${lettuce_output} | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"

#!/usr/bin/env bash

set -e

venv="./virtualenv"
lettuce_output="./nesi-webportal-test.out"

trap "rm -rf ${venv}; rm -f ${lettuce_output}" INT TERM EXIT

if [ ! -d ${venv} ]; then
  echo "############################ Create virtualenv ############################"
  rm -f ${venv}
  virtualenv ${venv}
  pip install -r requirements.pip > /dev/null
fi

echo "############################ Run selenium/lettuce tests ############################"
source ${venv}/bin/activate
lettuce > ${lettuce_output}
# purpose of call to sed: remove colors from lettuce output
cat ${lettuce_output} | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"

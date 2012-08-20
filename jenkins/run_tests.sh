#!/usr/bin/env bash

set -e

venv="virtualenv"
lettuce_output="nesi-webportal-test.out"

function on_exit {
  # purpose of call to sed: remove colors from lettuce output
  cat ${lettuce_output} | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"
  rm -f ${lettuce_output}
}

trap "on_exit" INT TERM EXIT

if [ ! -d ${venv} ]; then
  echo "############################ Create virtualenv ############################"
  rm -f ${venv}
  virtualenv ${venv}
  source ${venv}/bin/activate
  pip install -r requirements.pip
fi

echo "############################ Run selenium/lettuce tests ############################"
source ${venv}/bin/activate
lettuce > ${lettuce_output}

#!/usr/bin/env bash

echo "############################ Run selenium/lettuce tests ############################"
venv="/tmp/__tmp-nesi-webportal-test-virtualenv"
lettuce_output="/tmp/__tmp-nesi-webportal-test.out"
source ${venv}/bin/activate
lettuce > ${lettuce_output}
rc=$?
# purpose of call to sed: remove colors from lettuce output
cat ${lettuce_output} | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g"
exit ${rc}
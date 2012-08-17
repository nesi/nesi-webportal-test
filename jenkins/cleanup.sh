#!/usr/bin/env bash

set -e
echo "############################ Clean up ############################"
venv="/tmp/__tmp-nesi-webportal-test-virtualenv"
lettuce_output="/tmp/__tmp-nesi-webportal-test.out"
rm -rf ${venv}
rm -f ${lettuce_output}

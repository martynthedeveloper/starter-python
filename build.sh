#!/bin/bash
#set -x

RED='\033[0;31m'
BLUE='\033[0;34m'

function check_success() {
    result=$?
    if [ "$result" -ne 0 ]; then
      echo -e "$RED \nBuild failed"
    fi
}

if [[ -z "$VIRTUAL_ENV" ]]; then
  source venv/bin/activate
fi

pip3 install -r requirements.txt
check_success

coverage run -m pytest -vvs
check_success

coverage report -m
check_success

pylint --recursive=y src test
check_success

coverage html
check_success

echo -e "\033[1mReport: file://$PWD/htmlcov/index.html \033[m\n"

echo "Running: black --check src test"
black --check src test
check_success

echo -e "$BLUE \nBuild success"

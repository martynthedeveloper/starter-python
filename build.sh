#!/bin/bash
#set -x

RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

function check_success() {
  result=$?
  if [ "$result" -ne 0 ]; then
    echo -e "$RED \nBuild failed$NC"
  fi
}

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

if [[ -z "$VIRTUAL_ENV" ]]; then
  source source_me.sh
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

echo -e "$BLUE \nBuild success$NC"

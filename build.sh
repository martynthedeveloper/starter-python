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

uv run coverage run -m pytest -vvs
check_success

uv run coverage report -m
check_success

uv run pylint --recursive=y src test
check_success

uv run coverage html
check_success

echo -e "\033[1mReport: file://$PWD/htmlcov/index.html \033[m\n"

echo "Running: black --check src test"
uv run black --check src test
check_success

echo -e "$BLUE \nBuild success$NC"

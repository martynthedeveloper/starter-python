#!/bin/zsh


coverage run -m pytest -vvs

coverage report -m

pylint src test

coverage html

black --check src test

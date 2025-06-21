#!/bin/bash

# Exit on any error
set -e

echo "The following files will be removed:"
git clean -fxdn

read -p "Proceed ? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git clean -fxd
fi


#!/bin/bash
# Run this with source source_me.sh
if test -f "venv/Scripts/activate"; then
	source venv/scripts/activate
else
        source venv/bin/activate
fi

echo "Python Virtual environment activated."

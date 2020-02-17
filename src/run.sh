#!/bin/bash
#  script in the outer dir can execute directly
python3 main.py

# script int the inner dir depend on env PYTHONPATH
export PYTHONPATH=.
python3 dir002/main.py


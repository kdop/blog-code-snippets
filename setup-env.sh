#!/bin/bash

VENV_NAME="venv"

if [ -d $VENV_NAME ]
then
  python3 -m venv $VENV_NAME
fi

source venv/bin/activate
pip install -r requirements.txt
pre-commit install

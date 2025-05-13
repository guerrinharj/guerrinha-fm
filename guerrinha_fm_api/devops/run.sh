#!/bin/bash

export DJANGO_SETTINGS_MODULE=guerrinha_fm.settings
export PYTHONPATH=.

. .venv/bin/activate
daphne guerrinha_fm.asgi:application

#! /bin/bash
#
# run.sh
# Copyright (C) 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.
#


virtualenv .
bin/pip install -r requirements.txt
bin/python setup.py develop

bin/python monolith/app.py

#bin/celery worker -A monolith.background &


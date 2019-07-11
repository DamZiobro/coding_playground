#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.

"""

"""


import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

def read_file(filename):
    with open(filename) as f:
        data = yaml.load(f.read())

def run_command(cmd):
    return subprocess.check_call(cmd, shell=True)

db = create_engine('sqlite:///somedatabase')
Session = sessionmaker(bind=db)

def get_user(uid):
    session = Session()
    query = "select * from user where id='%s'" % uid
    return session.execute(query)

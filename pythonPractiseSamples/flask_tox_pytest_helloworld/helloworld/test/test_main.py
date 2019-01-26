#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

"""
Test main.py
"""

import pytest
from helloworld.main import app

@pytest.fixture
def flask_client():
    """fixture simulating flask_client"""
    app.config['TESTING'] = True
    client = app.test_client()

    yield client



def test_main():
    """docstring for test_main"""

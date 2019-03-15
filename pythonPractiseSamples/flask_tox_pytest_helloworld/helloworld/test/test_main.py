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

class TestFlaskApp(object):
    """TestFlaskApp"""

    @pytest.fixture
    def fixture_flask(self):
        """fixture simulating fixture_flask"""
        app.config['TESTING'] = True
        client = app.test_client()

        yield client

    def test_hello_world_route(self, fixture_flask):
        """docstring for test_main"""
        assert b'Hello World' in fixture_flask.get('/').data

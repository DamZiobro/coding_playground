#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import unittest

from app import hello

class TestHelloModule(unittest.TestCase):

    def test_hello_world_returns_hello_world(self):
        result = hello.hello_world()
        self.assertEqual("Hello, World!", result)

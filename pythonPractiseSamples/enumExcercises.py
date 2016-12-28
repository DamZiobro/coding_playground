#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
from enum import Enum

class Color(Enum):
    BLUE   = 1
    YELLOW = 2
    PINK   = 3
    RED    = 4

class TestPprintMethods(unittest.TestCase):

    def setUp(self):
        self.color = Color.BLUE

    def test_enum(self):
        self.assertEqual(self.color, Color.BLUE);

    def test_enum_value(self):
        self.assertEqual(self.color.value, 1);

if __name__ == "__main__": 
    print ("running unittests for enum")
    unittest.main();

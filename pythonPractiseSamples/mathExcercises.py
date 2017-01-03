#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import math

class TestMathMethods(unittest.TestCase):

    def setUp(self):
        self.number = 3.5
        self.negativeNumber = -3.5

    def test_ceil(self):
        self.assertEqual(math.ceil(self.number), 4);

    def test_fabs(self):
        self.assertEqual(math.fabs(self.negativeNumber), 3.5);

if __name__ == "__main__": 
    print ("running unittests for math")
    unittest.main();

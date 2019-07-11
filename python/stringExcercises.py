#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import datetime

class TestFunctoolsMethods(unittest.TestCase):

    def setUp(self):
        self.array      = [1,2,3,4,5,6,7,8,9]
        self.arrayShort = [1,2,3,4,5]
        self.array1     = [1,2,3]
        self.array2     = [4,5,6]

    def test_format(self):
        self.assertEqual('{} {} {}'.format("x", "y", "z"), "x y z")

    def test_format2(self):
        self.assertEqual('{2} {1} {0}'.format("x", "y", "z"), "z y x")

    def test_format3(self):
        self.assertEqual('{varB} {varA}'.format(varA="x", varB="y"), "y x")

    def test_datetime_format(self):
        d = datetime.datetime(2016,11,15, 8,27,30)
        self.assertEqual('{:%Y-%m-%d %H:%M:%S}'.format(d), "2016-11-15 08:27:30")

    def test_range(self):
        testArray = []
        for i in range (5,10):
            testArray.append(i)
        self.assertEqual(testArray, [5,6,7,8,9])

if __name__ == "__main__": 
    print ("running unittests for string")
    unittest.main();

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import datetime

class TestDatetimeMethods(unittest.TestCase):

    def setUp(self):
        self.sampleDate      = datetime.date(2016,11,23)
        self.sampleTime      = datetime.time(10,30,50)

    def test_dateConstructor(self):
        self.assertEqual(str(self.sampleDate), "2016-11-23")

    def test_timeConstructor(self):
        self.assertEqual(str(self.sampleTime), "10:30:50")


if __name__ == "__main__": 
    print ("running unittests for datetime")
    unittest.main();

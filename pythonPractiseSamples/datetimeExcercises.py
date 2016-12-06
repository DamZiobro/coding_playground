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

    def test_timedelta(self):
        self.assertEqual(str(datetime.timedelta(minutes=30, hours=8, seconds=20)), "8:30:20")

    def test_datetoday(self):
        self.assertEqual(str(datetime.date.today()), str(datetime.datetime.now().date()))

    def test_date_isoweekday(self):
        self.assertEqual(str(self.sampleDate.isoweekday()), "3")

    def test_date_fromordinal(self):
        self.assertEqual(str(datetime.date.fromordinal(735124)), "2013-09-13")

if __name__ == "__main__": 
    print ("running unittests for datetime")
    unittest.main();

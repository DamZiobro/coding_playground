#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import calendar

class TestCalendarMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_firstweekday(self):
        calendar.setfirstweekday(calendar.MONDAY)
        self.assertEqual(calendar.firstweekday(), calendar.MONDAY);

if __name__ == "__main__": 
    print ("running unittests for calendar")
    unittest.main();

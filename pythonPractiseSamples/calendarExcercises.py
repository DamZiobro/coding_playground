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

    def test_calendar_isleap(self):
        self.assertEqual(calendar.isleap(2016), True);
        self.assertEqual(calendar.isleap(2015), False);

    def test_calendar_weekheader(self):
        self.assertEqual(calendar.weekheader(5), " Mon   Tue   Wed   Thu   Fri   Sat   Sun ");

    def test_calendar_monthrange(self):
        self.assertEqual(calendar.monthrange(2016, 12), (3,31));

if __name__ == "__main__": 
    print ("running unittests for calendar")
    unittest.main();

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import pprint

class TestPprintMethods(unittest.TestCase):

    def setUp(self):
        self.myList = ['Damian', 'Madzia', 'Ziobro', 'Uram' ] 

    def test_dequeue_append(self):
        pprint.pprint(self.myList)
        self.assertEqual(pprint.pprint(self.myList), None);


if __name__ == "__main__": 
    print ("running unittests for pprint")
    unittest.main();

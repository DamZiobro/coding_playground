#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import difflib

class TestDifflibsMethods(unittest.TestCase):

    def setUp(self):
        self.array      = ['ape', 'apple', 'peach', 'puppy']

    def test_get_close_matches(self):
        self.assertEqual(difflib.get_close_matches('appel', self.array), ['apple', 'ape'])

    def test_get_close_matches_in_python_keywords(self):
        import keyword
        self.assertEqual(difflib.get_close_matches('wheil', keyword.kwlist), ['while'])

if __name__ == "__main__": 
    print ("running unittests for regular expressions")
    unittest.main();

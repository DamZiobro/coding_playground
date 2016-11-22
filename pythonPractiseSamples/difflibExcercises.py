#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
import difflib
import textwrap

class TestDifflibsMethods(unittest.TestCase):

    def setUp(self):
        self.array      = ['ape', 'apple', 'peach', 'puppy']

    def test_get_close_matches(self):
        self.assertEqual(difflib.get_close_matches('appel', self.array), ['apple', 'ape'])

    def test_get_close_matches_in_python_keywords(self):
        import keyword
        self.assertEqual(difflib.get_close_matches('wheil', keyword.kwlist), ['while'])

    def test_SequenceMatcher_Ratio(self):
        s = difflib.SequenceMatcher(None, "abcd", "bcde")
        self.assertEqual(s.ratio(), 0.75)

    def test_testwrap(self):
        s = textwrap.shorten("Damian Ziobro", 13)
        self.assertEqual(s, "Damian Ziobro")
        s = textwrap.shorten("Damian Ziobro", 12)
        self.assertEqual(s, "Damian [...]")


if __name__ == "__main__": 
    print ("running unittests for regular expressions")
    unittest.main();

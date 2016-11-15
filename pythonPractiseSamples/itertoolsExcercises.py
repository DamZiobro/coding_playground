#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import itertools
import unittest

class TestItertoolsMethods(unittest.TestCase):

    def setUp(self):
        self.array      = [1,2,3,4,5,6,7,8,9]
        self.arrayShort = [1,2,3,4,5]
        self.array1     = [1,2,3]
        self.array2     = [4,5,6]

    def test_accumulate(self):
        self.assertEqual(tuple(itertools.accumulate(self.array)), (1,3,6,10,15,21,28,36,45))

    def test_chain(self):
        self.assertEqual(tuple(itertools.chain(self.array1, self.array2)), (1,2,3,4,5,6))

    def test_islice(self):
        self.assertEqual(tuple(itertools.islice(self.array, 2,4)), (3,4)) #as we number from 0
        self.assertEqual(len(tuple(itertools.islice(self.array, 2,7))), 5)

    def test_compress(self):
        self.assertEqual(tuple(itertools.compress(self.arrayShort, [1,0,1,0,1])), (1,3,5)) #as we number from 0
        self.assertEqual(len(tuple(itertools.compress(self.arrayShort, [1,0,1,0,1]))), 3)
        
    def test_dropwhile(self):
        result = tuple(itertools.dropwhile(lambda x: x<5, self.array))
        self.assertEqual(result, (5,6,7,8,9)) #as we number from 0
        self.assertEqual(len(result), 5) #as we number from 0

    def test_takewhile(self):
        result = tuple(itertools.takewhile(lambda x: x<5, self.array))
        self.assertEqual(result, (1,2,3,4)) #as we number from 0
        self.assertEqual(len(result), 4)

    def test_takewhile(self):
        result = tuple(itertools.takewhile(lambda x: x<5, self.array))
        self.assertEqual(result, (1,2,3,4)) #as we number from 0
        self.assertEqual(len(result), 4)

if __name__ == "__main__": 
    print ("running unittests for itertools")
    unittest.main();

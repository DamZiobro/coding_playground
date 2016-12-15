#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
from collections import deque

class TestCollectionsMethods(unittest.TestCase):

    def setUp(self):
        self.deq = deque("ghi")

    def test_dequeue_append(self):
        self.deq.append('j')
        self.assertEqual(self.deq[0], 'g');
        self.assertEqual(self.deq[-1], 'j');

if __name__ == "__main__": 
    print ("running unittests for collections")
    unittest.main();

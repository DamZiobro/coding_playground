#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

import unittest
from collections import deque
from collections import defaultdict
from collections import namedtuple
from collections import Counter
from collections import OrderedDict

class TestCollectionsMethods(unittest.TestCase):

    def setUp(self):
        self.deq = deque("ghi")
        self.myList = [('x', 5), ('y', 10), ('a', 3), ('f', 6), ('e', 2)]
        self.dict = defaultdict(list)
        for k,v in self.myList:
            self.dict[k].append(v)

    def test_dequeue_append(self):
        self.deq.append('j')
        self.assertEqual(self.deq[0], 'g');
        self.assertEqual(self.deq[-1], 'j');

    def test_dequeue_popleft(self):
        self.deq.popleft()
        self.assertEqual(self.deq[0], 'h');
        self.assertEqual(self.deq[-1], 'i');

    def test_defaultdict_sorted_and_slicing(self):
        self.assertEqual(sorted(self.dict.items()), [('a', [3]), ('e', [2]), ('f', [6]), ('x', [5]), ('y', [10])]);

    def test_namedtuple(self):
        Point3D = namedtuple('Point3D', ['x', 'y', 'z'])
        p = Point3D(10,z=20,y=12)
        self.assertEqual(p.x+p.y+p.z, 42);

    def test_counter(self):
        counter = Counter("Damian Ziobro")
        self.assertEqual(counter['o'], 2);

    def test_OrderedDict(self):
        dict = OrderedDict.fromkeys("Damian") #overridden 2nd 'a' as this is dict
        dict.move_to_end("m")
        self.assertEqual(''.join(dict.keys()), "Dainm");


if __name__ == "__main__": 
    print ("running unittests for collections")
    unittest.main();

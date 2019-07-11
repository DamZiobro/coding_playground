#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

"""
Python notepad
"""


from __future__ import print_function
import bisect
from itertools import *
from operator import *

values = [3,6,2,1,7,6,3,5]

print('==========================================================================================')
print("test bisect")

l = []
for v in values:
    bisect.bisect(l, v)
    bisect.insort(l, v)
    print(l)

print('==========================================================================================')
print("test LifoQueue")
import queue

q = queue.LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end=' ')
print('\n')

print('==========================================================================================')
print("test map")

for i in map(lambda x: x*2, range(0, 5)):
    print(i)

print('==========================================================================================')
print("test list comperhension")
for i in [x*2 for x in range(0, 5)]:
    print(i)

print('==========================================================================================')
print("test zip count repeat")
for i in zip(count(), repeat('damian', 5)):
    print('{}: {}'.format(*i))

print('==========================================================================================')
print("test cycle")
for i in zip(range(0,5), cycle(['damian', 'ziobro'])):
    print('{}: {}'.format(*i))

print('==========================================================================================')
print("test cycle")
print(list(accumulate('abcde')))

print('==========================================================================================')
print("arg getter example")

class SampleClass(object):
    """docstring for """
    def __init__(self, identity):
        self._id = identity

    def __repr__(self):
        return 'SampleClass({})'.format(self._id)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, identity):
        self._id = identity

l = [SampleClass(i) for i in range(5)]
# getting ids
getter = attrgetter('id')
ids = [getter(obj) for obj in l]
print("ids: {}".format(ids))

print('==========================================================================================')
print("test decimal and context")

import decimal

dec_num = decimal.Decimal("0.12345")

for i in range(1, 5):
    decimal.getcontext().prec = i
    decimal.getcontext().rounding = ROUND_HALF_EVEN
    print("{:8}: {}".format(dec_num, dec_num * 1))

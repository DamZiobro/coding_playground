#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Damian Ziobro <damian@xmementoit.com>

"""
testing __init__, __del__ and property
"""


class Counter(object):

    @property
    def counter(self):
        print("Get counter")
        return self._counter

    @counter.setter
    def counter(self, value):
        print("Set counter")
        self._counter = value

    def __init__(self, value):
        super(Counter, self).__init__()
        print("Constructor")
        self._counter = value

    def __del__(self):
        print("Destructor")

x = Counter(3)
print(x.counter)
x.counter = 4
print(x.counter)
        

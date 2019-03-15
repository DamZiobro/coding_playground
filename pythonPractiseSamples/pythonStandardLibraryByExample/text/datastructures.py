#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

"""
Testing Python data structures (set, list tuple dict etc.)
"""
from __future__ import print_function

import enum
from collections import Counter


class BugStatus(enum.Enum):
    """Bug statuses"""
    NEW = 7
    INCOMPLETE = 6
    INVALID = 5
    WONT_FIX = 4
    IN_PROGRESS = 3
    FIX_COMMITED = 2
    FIX_RELEASED = 1


class DataStructures(object):
    """docstring for DataStructures"""
    def __init__(self):
        """constructor"""
        self._counter = Counter('abbcdda')

    @property
    def counter(self):
        '''get counter'''
        return self._counter

    @counter.setter
    def counter(self, counter):
        '''set new counter'''
        self._counter = counter

    def print_all_bug_statuses(self):
        """display bug statuses in pretty print"""
        for status in BugStatus:
            print('{:15}:{}'.format(status.name, status.value))

    def add_to_counter(self, *values):
        '''add values to counter property'''
        for value in values:
            self._counter.update(value)

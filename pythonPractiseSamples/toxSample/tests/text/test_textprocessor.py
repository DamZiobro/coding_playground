#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

"""
Unit tests related to text.py
"""
import unittest
from text.datastructures import DataStructures

class TestDataStructures(unittest.TestCase):
    """
    DataStructures test cases
    """

    def setUp(self):
        self.structures = DataStructures()

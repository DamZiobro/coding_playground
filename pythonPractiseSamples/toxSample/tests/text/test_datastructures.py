#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

"""
Unit tests 
"""
import unittest
from text.datastructures import DataStructures

class TextTest(unittest.TestCase):
    """
    TextProcessor test cases
    """

    def setUp(self):
        self.structures = DataStructures()

    def test_add_to_update_properly_updates_values(self):
        '''test add_to_counter test'''

        counter = self.structures.counter

        start_elems = dict(counter)
        self.structures.add_to_counter('aabb', 'ccdd')
        self.structures.add_to_counter({'a' : 3, 'd' : 5})
        end_elems = dict(counter)

        self.assertEqual(end_elems['a'], start_elems['a'] + 5)
        self.assertEqual(end_elems['d'], start_elems['d'] + 7)

    def test_add_to_update_throw_if_constant_argument(self):
        '''test whether add_to_counter'''
        with self.assertRaises(TypeError):
            self.structures.add_to_counter(10)

    def test_zip_works_as_expected(self):
        '''test standard zip function'''
        tuple1 = ('Damian', 'Mike', 'Johny')
        tuple2 = ('Chloe', 'Jessica', 'Cheryl')

        self.assertTrue(
            self.structures.zip_test(tuple1, tuple2)[1],
            ('Mike', 'Jessica')
        )

    def test_reduce_by_add(self):
        '''test functools.reduce'''
        values = range(1, 5)
        self.assertTrue(self.structures.reduce_values_by_add(values), 10)

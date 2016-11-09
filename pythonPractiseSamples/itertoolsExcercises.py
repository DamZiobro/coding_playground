#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

"""

"""
import itertools

print ("--------------------------------------------------------------------------------")
array = [1,2,3,4,5]
print ("accumulate:")
for element in itertools.accumulate(array):
    print(element)

array1 = [1,2,3]
array2 = [4,5,6]
print ("--------------------------------------------------------------------------------")
print ("chain:")
for element in itertools.chain(array1, array2):
    print (element)

    

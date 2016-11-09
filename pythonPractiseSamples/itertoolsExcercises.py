#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Damian Ziobro <damian@xmementoit.com>

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

print ("--------------------------------------------------------------------------------")
print ("islice:")
for element in itertools.islice(array, 2, 4):
    print (element)
    

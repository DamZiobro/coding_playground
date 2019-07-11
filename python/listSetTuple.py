#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.

"""
Testing list, set and tuple, dict and generator
"""

if __name__ == "__main__":    
    lst = [value for value in range(10) if value %2 == 0]
    print(lst)
    tup = tuple(lst)
    print(tup)
    gen = (value for value in range(10) if value %2 == 0)
    print(gen)
    for item in gen:
        print item
    myset = {value for value in range(10) if value %2 == 0}
    print(myset)
    myset.add(5);
    myset.add(4); #this is not applied as '4' already exists in set
    print(myset)
    dct = {value : str(value) for value in range(10) if value % 2 == 0}
    print(dct)


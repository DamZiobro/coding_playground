#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017 Damian Ziobro <damian@xmementoit.com>
#
# Distributed under terms of the MIT license.


import resource

class TestClass(object):
    """docstring for TestClass"""
    
    #defining slots to reduce usage more memory of class TestClass
    #by informing Python interpreter that dynamic dict does not need to be 
    #created
    # memory usage or list of 10000 objects of TestClass is as follows:
    #  - with __slots__   defined (uncomment below line) -  9156 KB 
    #  - with __slots__ undefined (comment   below line) - 11788 KB (23% more)
    __slots__ = ('arg1', 'arg2', 'arg3', 'arg4', 'arg5')

    def __init__(self, value):
        self.arg1 = value +1
        self.arg2 = value +2
        self.arg3 = value +3
        self.arg4 = value +4
        self.arg5 = value +5


def create_list_of_TestClass_objects(count):
    """
    function create list containing TestClass objects
    :param count: number of object to create and append to list
    :return: list of 'count' number of TestClass objects
    """
    lst = []

    for i in range(count):
        test = TestClass(i)
        lst.append(test)

    return lst

if __name__ == "__main__":    
    count = 10000
    lst = create_list_of_TestClass_objects(count)

    #calculate memory usage of class
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print "Memory usage is; {0} KB".format(mem)
    print "Avarage size of TestClass object is; {0} KB".format(float(mem)/count)
        

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2017 Damian Ziobro <damian@xmementoit.com>
#
# Distributed under terms of the MIT license.


import resource
import gc
import objgraph

class TestClass(object):
    """docstring for TestClass"""
    #uncomment this line and see the generated graph => lst-references.png in
    #order to visually check how __slots__ saves memory
    __slots__ = ('arg1', 'arg2', 'arg3', 'arg4', 'arg5')

    def __init__(self, value):
        self.arg1 = value +1
        self.arg2 = value +2
        self.arg3 = value +3
        self.arg4 = value +4
        self.arg5 = value +5


def create_list_of_testclass_objs(count):
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
    COUNT = 1
    LST = create_list_of_testclass_objs(COUNT)

    #calculate and prting general memory usage
    MEM = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print "Memory usage is; {0} KB".format(MEM)
    print "Avarage size of TestClass object is; {0} KB".format(float(MEM)/COUNT)

    #invoke Garbage Collector explicitely in order to
    #collect non longer used memory before investigating memory leak
    gc.collect()

    #show object of which types consumes most of memory
    objgraph.show_most_common_types()
    #build graph of reference of lst object - it takes long time to generate
    # (up to few minutes)
    # DIAGNOSTICS ONLY - DON'T USE IN PRODUCTION CODE
    objgraph.show_refs(LST, filename='lst-references.png')

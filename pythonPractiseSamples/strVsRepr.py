#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Damian Ziobro <damian@xmementoit.com>

"""
Testing difference between __str__ and __repr__
"""

class ReprStrTest(object):
    """class to test __str__ and __repr__"""
    def __init__(self, name):
        super(ReprStrTest, self).__init__()
        self.name = name
        self.arg2 = "default value"

    def __str__(self):
        """return 'name' structure when invoked __str__"""
        return str(self.name)

    def __repr__(self):
        """return __dict__ structure when invoked __repr__"""
        return str(self.__dict__)

if __name__ == "__main__":    
    obj = ReprStrTest("test");

    print "str : {0}".format(str(obj))
    print "repr: {0}".format(repr(obj))
        
        


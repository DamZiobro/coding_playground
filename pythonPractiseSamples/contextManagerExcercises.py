#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-work>
#
# Distributed under terms of the MIT license.


class MyContextmanager():
    """docstring for MyContextmanager"""
    def __init__(self):
        print("MyContextmanager::constructor()")

    def __enter__(self):
        print("MyContextmanager::__enter__")

    def __exit__(self, type, value, traceback):
        print("MyContextmanager::__exit__")

if __name__ == "__main__":    
    with MyContextmanager() as ctx:
        print "ctx - body"

        

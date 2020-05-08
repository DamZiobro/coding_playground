#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import traceback

def function5():
    print("function5")
    raise TypeError("Oups!")

def function4():
    print("function4")
    function5()

def function3():
    print("function3")
    function4()

def function2():
    print("function2")
    function3()
    

def function1():
    print("function1")

    try:
        function2()
    except Exception as err:
        try:
            raise TypeError("Again !?!")
        except:
            pass

        print(f"EXCEPTION CAUGHT => TRACEBACK OF EXCEPTION BELOW")
        trace = traceback.print_exc()

function1()
print("continue")

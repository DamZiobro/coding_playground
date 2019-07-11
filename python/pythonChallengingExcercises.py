#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

"""
Execrcises and Based on https://github.com/zhiwehu/Python-programming-exercises
"""

import math


def list_div_by_7_but_not_5(start=2000, stop=3200):
    """
    Question1: 
    all numbers divisible by 7 but not by 5 from selected range
    """

    return ','.join([ str(value) for value in range(start,stop+1) \
            if value%7 == 0 and value%5 != 0 ])

def factorial_of_items(*numbers):
    """
    Question2:
    print comma-separate factorials of the given numbers
    """
    def factorial(num):
        if num == 0:
            return 1
        return num * factorial(num-1)
    return ','.join([ str(factorial(number)) for number in numbers ])
    #return ','.join([ str(math.factorial(number)) for number in numbers ])
    
def dict_of_integrals_until(num):
    """
    Question3:
    print dict of integrals from 0 to 'num' containing pairs {num: num*num}
    """
    return {i : i*i for i in range(1,num+1)}

def string_to_list(comma_sep_str):
    """
    Question4:
    returns list of comma-separate string containing numbers
    """
    l = [ i for i in comma_sep_str.split(',')]
    return l, tuple(l)


if __name__ == "__main__":
    print list_div_by_7_but_not_5()
    print factorial_of_items(8,10,12)
    print dict_of_integrals_until(8)
    print string_to_list("34,67,55,33,12,98")
    

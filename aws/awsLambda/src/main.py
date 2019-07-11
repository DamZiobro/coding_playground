#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
Hello world AWS lambda function
"""

def handler(event, context):
    message = 'Hello World!'
    return { 'message' : message }  

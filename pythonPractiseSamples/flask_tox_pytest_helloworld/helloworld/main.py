#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.

"""

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    '''hello_world'''
    return 'Hello World'

if __name__ == "__main__":    
    app.run()

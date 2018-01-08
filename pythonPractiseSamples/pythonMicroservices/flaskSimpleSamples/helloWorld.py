#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Damian Ziobro <damian@xmementoit.com>

"""
Flask - Hello World
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    return jsonify({'Hello': 'World'})

if __name__ == "__main__":    
    app.run()

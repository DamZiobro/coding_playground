#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Damian Ziobro <damian@xmementoit.com>

"""
Flask - Hello World
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def my_microservice():
    #request is global variable in Flask views (functions decorated by app.route())
    print (request)
    print (request.environ)
    response = jsonify({'Hello': 'World'})
    print (response)
    print (response.authorization)
    print (response.data)
    return response


#Using variables to get dynamic-based routes
@app.route('/api/<var_id>')
def my_microservice2(var_id):
    return jsonify({'Hello': var_id})
    

if __name__ == "__main__":    
    print(app.url_map)
    app.run()

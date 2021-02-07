#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('templates.html', marks = score)

if __name__ == '__main__':
   app.run(debug = True)

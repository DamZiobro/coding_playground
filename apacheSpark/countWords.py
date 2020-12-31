#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

import pyspark
sc = pyspark.SparkContext('local[*]')
#sc.setLogLevel("INFO")

txt = sc.textFile('file:////usr/share/doc/python3/copyright')
python_lines = txt.filter(lambda line: 'python' in line.lower())

with open('results.txt', 'w') as file_obj:
    file_obj.write(f'Number of lines: {txt.count()}\n')
    file_obj.write(f'Number of lines with python: {python_lines.count()}\n')

print(f'Number of lines: {txt.count()}')
print(f'Number of lines with python: {python_lines.count()}')

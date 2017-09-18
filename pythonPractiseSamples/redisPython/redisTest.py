#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Damian Ziobro <damian@xmementoit.com>
#
# Distributed under terms of the MIT license.

"""
This is hello world application to use Redis NoSQL databas
"""

import redis

REDIS = redis.Redis(host='localhost', port=5000, password='password')
REDIS.set('key', 'value')
VALUE = REDIS.get('key')
print str(VALUE)

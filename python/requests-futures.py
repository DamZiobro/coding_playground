#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

session = FuturesSession()
# first request is started in background
future_one = session.get('http://httpbin.org/get')
# second requests is started immediately
future_two = session.get('http://httpbin.org/get?foo=bar')
# wait for the first request to complete, if it hasn't already
response_one = future_one.result()
print('response one status: {0}'.format(response_one.status_code))
print(response_one.content)
# wait for the second request to complete, if it hasn't already
response_two = future_two.result()
print('response two status: {0}'.format(response_two.status_code))
print(response_two.content)

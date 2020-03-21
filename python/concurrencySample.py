#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import time
import requests
import logging
from concurrent import futures

logging.getLogger().setLevel(logging.INFO)

def fetch_url(im_url):
    try:
        resp = requests.get(im_url)
    except Exception as e:
        logging.info("could not fetch {}".format(im_url))
    else:
        return resp.content
        

def fetch_all(url_list):
    with futures.ThreadPoolExecutor() as executor:
        responses = executor.map(fetch_url, url_list)
    return responses
    

if __name__=='__main__':
    
    url = "http://dummy.restapiexample.com/api/v1/employees"

    for ntimes in [1, 10, 100]:
        start_time = time.time()
        responses = fetch_all([url] * ntimes)
        logging.info('Fetch %s urls takes %s seconds', ntimes, time.time() - start_time)

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

import requests
import sys
from generic_decorators import make_parallel, timing, make_parallel_processes


def sample_function(post_id):
    """
        Just a sample function which would make dummy API calls
    """

    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

@timing
def serial_function_trigger():
    print(" -> start 'serial_function_trigger'")
    list_of_post_ids = list(range(1, 20))

    # Serial way of calling the function
    results = []
    for post_id in list_of_post_ids:
        res = sample_function(post_id)
        results.append(res)
    return results

@timing
def parallel_function_trigger():# Paralleized way of calling the function
    print(" -> start 'parallel_function_trigger'")
    list_of_post_ids = list(range(1, 20))
    return make_parallel(sample_function)(list_of_post_ids)

@timing
def parallel_multiprocessing_function_trigger():# Paralleized way of calling the function
    print(" -> start 'parallel_multiprocessing_function_trigger'")
    list_of_post_ids = list(range(1, 20))
    return make_parallel_processes(sample_function)(list_of_post_ids)

def main():
    ret1 = serial_function_trigger()
    ret2 = parallel_function_trigger()
    ret3 = parallel_multiprocessing_function_trigger()

    #print(f"results: {ret3}")

if __name__ == "__main__":
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import asyncio
import time
import requests
import httpx 

class S3BatchProcessor(object):
    """docstring for S3BatchProcessor"""

    def execute(self):
        url = "http://httpbin.org/get"

        #synchronous - blocking function requests.get()
        #resp = requests.get(url)

        #asynchronous - non-blocking function AsyncClient.get()
        #client = httpx.AsyncClient()
        #resp = await client.get(url)

        time.sleep(1)

        #await asyncio.sleep(1)

def process_batch(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"process_batch {name}: Compute factorial({i})...")
        S3BatchProcessor().execute()
        f *= i
    print(f"process_batch {name}: factorial({number}) = {f}")
    return f

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

async def process_batches(loop):
    # Schedule three calls *concurrently*:
    
    batch_processors_futures = [loop.run_in_executor(None, process_batch, letter, ord(letter) - ord("A") + 2) for letter in char_range("A", "D")]

    for future in batch_processors_futures:
        batch_processor = await future
        print(f"Batch_processor: {batch_processor}")

if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_batches(loop))

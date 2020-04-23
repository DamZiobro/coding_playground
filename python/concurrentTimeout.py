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
import concurrent.futures
import threading

class S3BatchProcessor(object):
    """docstring for S3BatchProcessor"""

    def __init__(self):
        self.trigger_number = 0

    def execute(self, requests_lock):

        self.trigger_number = self.trigger_number + 1

        SLEEP_TIME_SECONDS = 1
        if self.trigger_number == 10:
            SLEEP_TIME_SECONDS = 5

        time.sleep(SLEEP_TIME_SECONDS)

def process_batch(name, number, requests_lock):
    f = 1
    for i in range(2, number + 1):
        print(f"process_batch {name}: Compute factorial({i})...")
        S3BatchProcessor().execute(requests_lock)
        f *= i
    print(f"process_batch {name}: factorial({number}) = {f}")
    return f

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

async def process_batches(loop):
    # Schedule three calls *concurrently*:
    requests_lock = threading.Lock()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    batch_processors_futures = [loop.run_in_executor(executor, process_batch, letter, ord(letter) - ord("A") + 2, requests_lock) for letter in char_range("A", "H")]

    batch_processors = []
    for future in batch_processors_futures:
        batch_processor = await future
        batch_processors.append(batch_processor)
        print(f"Batch_processor: {batch_processor}")

    print(f"Processors = {batch_processors}")

if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process_batches(loop))

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import time
import concurrent.futures
import threading
import os
from retrying import retry

class MoriTimeoutException(Exception):
    pass
        

@retry(stop_max_attempt_number=3, retry_on_exception=MoriTimeoutException)
class BatchProcessor(object):
    """docstring for BatchProcessor"""

    def __init__(self):
        self.max_osp_api_threads = 3
        self.batch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def update_osp_api(self, item):

        pid = os.getpid()
        print(f"item: {item}; pid: {pid}")

        sleep_time_seconds = 1
        if item % 3 == 0:
            sleep_time_seconds = 10 #wait forever

            try:
                raise MoriTimeoutException()
            except MoriTimeoutException as ex:
                print("MORI_TIMEOUT_EXCEPTION")
                raise ex

        print(f"Sleeping {sleep_time_seconds} seconds")
        time.sleep(sleep_time_seconds)
        return item

    def process_osp_api_response(self, item, osp_api_response):
        print(f"process_osp_api_response: {item}")
       
    def retry_process(self, retry_items):
        self.process(retry_items)
        
    def process(self, retry_batch=None):
        if retry_batch != None:
            self.batch = retry_batch
        retry_items = []
        TIMEOUT_SECONDS=2
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_osp_api_threads) as executor:
            try:
                item_futures = {executor.submit(self.update_osp_api, item): item for item in self.batch}
            except Exception as ex:
                print(f"exception: {ex}")

            for future in concurrent.futures.as_completed(item_futures):
                #try:
                    item = item_futures[future]
                    osp_api_response = None
                    try:
                        osp_api_response = future.result(timeout=TIMEOUT_SECONDS)
                    except Exception as ex:
                        print(f"SomeException for item: {item}")

                    if osp_api_response is not None:
                        self.process_osp_api_response(item, osp_api_response)
                #except concurrent.futures.TimeoutError:
                    #print(f"TimeoutError for item: {item}")
                    #retry_items.append(item)
                    #executor.shutdown(wait=False)
                    #is_cancelled = future.cancel()
                    #print(f"isCancelled: {is_cancelled}")

        if retry_batch == None and len(retry_items) > 0:
            print(f"retry_items: {retry_items}")
            self.retry_process(retry_items)


                    

if __name__ == "__main__":    
    processor = BatchProcessor()
    processor.process()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import time
from random import randint
from retrying import retry
import requests
from timeout_decorator import TimeoutError, timeout


@retry(stop_max_attempt_number=3)  # stop after 6 attempts
@timeout(1)
def long_running_function():
    sleep_time = randint(0,9)
    print("Doing something that takes " + str(sleep_time) + " seconds...")
    requests.get("http://ipv4.download.thinkbroadband.com/1GB.zip", verify=False)
    print("Finished!")


try:
    long_running_function()
except TimeoutError:
    print("Timeout!")

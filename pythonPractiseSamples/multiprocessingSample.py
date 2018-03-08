#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

"""
Testing multiprocessing for spawning class method

"""

import multiprocessing
import time
import random

class Processing(object):
    def __init__(self, name):
        self.name = name
    def process(self):
        sleep_time = random.randint(0,10)
        print("task: {}; sleep: {}".format(self.name, sleep_time))
        time.sleep(sleep_time)
        print("processing: {}".format(str(self.name)))


if __name__ == "__main__":    
    processings = []
    for i in range(0,10):
        processings.append(Processing(str(i)))

    cpus = multiprocessing.cpu_count()-1;
    print("nr of cpus: {}".format(cpus))
    if cpus > 1:
        processes = []
        for processing in processings:
            p = multiprocessing.Process(target=processing.process)
            p.start()
            processes.append(p)
        #wait until processes will finish
        [p.join() for p in processes]

    else:
        for processing in processings:
            processing.process()
        
print("Finish")



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

class Processing(object):
    def __init__(self, name):
        self.name = name
    def process(self):
        sleep_time=2
        print("processing task: {}; sleep: {}".format(self.name, sleep_time))
        time.sleep(sleep_time)
        print("finish {}".format(str(self.name)))

def invoke_process(processing):
    return processing.process()


if __name__ == "__main__":    
    processings = []
    for i in range(0,10):
        processings.append(Processing(str(i)))

    cpus = multiprocessing.cpu_count()-1;
    print("nr of cpus: {}".format(cpus))
    if cpus > 1:
        p = multiprocessing.Pool(processes=cpus)
        p.map(invoke_process, processings)
    else:
        for processing in processings:
            processing.process()
        
print("Finish")



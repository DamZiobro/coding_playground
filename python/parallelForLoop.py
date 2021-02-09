#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Damian Ziobro <damian@xmementoit.com>
#

from joblib import Parallel, delayed
import multiprocessing

n=10000

def squareRoot(i):
    return i*i

cpus = multiprocessing.cpu_count()
#cpus = 1

results = Parallel(n_jobs=cpus)(delayed(squareRoot)(i) for i in range(n))
print(results)

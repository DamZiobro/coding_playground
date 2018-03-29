#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Hello World application using matplotlib 
"""


import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.05)
print t

s = np.sin(2 * np.pi * t)
print s

#make line blue
plt.rcParams['lines.color'] = 'r'
plt.plot(t,s)

c = np.cos(2 * np.pi * t)
#make line thick
plt.rcParams['lines.linewidth'] = '3'
plt.plot(t,c)

plt.show()


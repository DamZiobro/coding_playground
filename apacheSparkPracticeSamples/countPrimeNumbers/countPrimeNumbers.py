#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""
Counting primer numbers from 0 to 10000000 with help of Apache Spark map-reduce 
+ compare time of parallel (Spark-based) vs sequantial calculation

To see parallelism of apache spark you can open 'top' command in separate 
terminal while running this script
"""

import sys
try:
    import pyspark
except ImportError:
    print("ERROR: pyspark module not installed. Use 'sudo pip install pyspark'")
    sys.exit(1)

NUMBERS_THRESHOLD=10000000

#running Apache Spark
if not 'sc' in globals():
    sc = pyspark.SparkContext()


#timeit decorator
def timeit(method):
    def timed(*args, **kw):
        import time
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("time of execution method {}: {} ms".format(str(method.__name__),int((te-ts)*1000)))
    return timed

def is_it_prime(number):
    # make sure n is a positive integer
    number = abs(int(number))
    # simple tests
    if number < 2:
        return False
    # 2 is prime
    if number == 2:
        return True
    # other even numbers aren't
    if not number & 1:
        return False
    # check whether number is divisible into it's square root
    for x in range(3, int(number**0.5)+1, 2):
        if number % x == 0:
            return False
    #if we get this far we are good
    return True

@timeit
def parallelSparkBasedCalculation():

    # create a set of numbers to 
    numbers = sc.parallelize(xrange(NUMBERS_THRESHOLD))
    # count out the number of primes we found
    count = numbers.filter(is_it_prime).count()
    print("parallelSparkBasedCalculation result: {}".format(count))

@timeit
def sequantialCalculation():
    count = 0
    for i in xrange(NUMBERS_THRESHOLD):
        if (is_it_prime(i)):
            count+=1
    print("sequantialCalculation result: {}".format(count))

if __name__ == "__main__":    
    sequantialCalculation()
    parallelSparkBasedCalculation() 


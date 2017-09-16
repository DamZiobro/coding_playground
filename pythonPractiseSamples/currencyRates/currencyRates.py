#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

"""
Test app for BeautifulSoap practice. It scraps currency rates for from xc.com
"""


from bs4 import BeautifulSoup
import requests

URL_TEMPLATE="http://www.xe.com/currencyconverter/convert?Amount=1&From={fromCurr}&To={toCurr}"

currpairs = [
    ('GBP', 'PLN'), 
    ('GBP', 'USD'),
    ('GBP', 'EUR'),
    ('EUR', 'PLN'),
    ('USD', 'PLN'),
    ('CHF', 'PLN'),
             ]

if __name__ == "__main__": 
    for currpair in currpairs: 
        CURR_URL = URL_TEMPLATE.format(fromCurr=currpair[0], toCurr=currpair[1])
        r = requests.get(CURR_URL)
        data = r.text

        soup = BeautifulSoup(data)
        currrates = soup.find('span', attrs={'class': 'uccResultAmount'})
        if currrates is None:
            print "ERROR: cannot get exchange from " \
                  "{0} to {1}".format(currpair[0], currpair[1])
        else:
            print "{} <=> {}: {:0.2f}".format(currpair[0], currpair[1], \
                                            float(str(currrates.text)))

        data = soup.find_all('script', {'type' : 'text/javascript'})


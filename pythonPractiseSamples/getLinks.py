#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

"""
Get http and https links from selected website
"""

from BeautifulSoup import BeautifulSoup
import urllib2
import re
import sys

def usage():
    print("ERROR: wrong arguments")
    print("Usage: {} urlToScrap".format(sys.argv[0]))

def getLinks(url):
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []
 
    for link in soup.findAll('a', attrs={'href': re.compile("^http[s]?://")}):
        links.append(link.get('href'))
 
    return links

if __name__ == "__main__":    

    if (len(sys.argv) != 2):
        usage()
        sys.exit(100)

    url = sys.argv[1]

links = getLinks(url)

for link in links:
    print link

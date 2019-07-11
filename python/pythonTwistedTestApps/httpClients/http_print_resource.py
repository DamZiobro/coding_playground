#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
"""
Print body of web page
"""

from twisted.internet import reactor
from twisted.web.client import getPage
import sys 

def print_page(page_content):
    print page_content

def print_error(failure):
    print sys.stderr>>failure

def stop(result):
    reactor.stop() 

if (len(sys.argv) != 2 ): 
    print >> sys.stderr,"Usage: " + sys.argv[0] + " URL"
    exit(-1)

METHOD="POST"
d = None

if METHOD == "GET":
    d = getPage(sys.argv[1], method=METHOD)
else:
    POST_DATA="My post data"
    d = getPage(sys.argv[1], method=METHOD, postdata=POST_DATA)

d.addCallbacks(print_page, print_error);
d.addBoth(stop)

reactor.run()

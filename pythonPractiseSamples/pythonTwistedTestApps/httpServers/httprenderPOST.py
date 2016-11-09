#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""
HTTP Server demonstrating how to get and render HTTP POST requests
"""

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

class TestPage(Resource):
    isLeaf = True
    def render_POST(self, request):
        print "POST: Received content: " + request.content.read()
        return request.content.read()[::-1]
    def render_GET(self, request):
        print "GET: Received content: " + request.content.read()
        return request.content.read()[::-1]

resource = TestPage()
factory = Site(resource)

reactor.listenTCP(8000, factory)
reactor.run()

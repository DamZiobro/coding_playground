#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
HTTP dynamic content site + dispatches
"""

from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from twisted.web.util import redirectTo

from calendar import calendar
from datetime import datetime

class YearPage(Resource):
    #if isLeaf set to true, then /2015 will be rendered the same way as /2015/aaa, /2015/xxx, /2015/aa/aa
    #isLeaf = True
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year))

class CalendarHomeDispatcher(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()

    def render_GET(self, request):
        #return "<html><body>Welcome to the calendar server! </body></html>"
        #redirect to current year child page
        return redirectTo(datetime.now().year, request)

resource = CalendarHomeDispatcher()
reactor.listenTCP(8000, Site(resource))
reactor.run()

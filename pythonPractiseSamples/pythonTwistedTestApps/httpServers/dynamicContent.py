#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
HTTP Static content site
"""

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import time

class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return "This local time is %s" % (time.ctime(),)

resource = ClockPage()
reactor.listenTCP(8000, Site(resource))
reactor.run()

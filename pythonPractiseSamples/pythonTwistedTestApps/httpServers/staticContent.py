#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
HTTP Static content site
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

reactor.listenTCP(8000, Site(File('/var/www/html/')))
reactor.run()

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
HTTP Static content site + dispatches
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

root = File("/var/www/html")
root.putChild("log", File("/var/log/syslog"))
root.putChild("doc", File("/usr/share/doc"))
reactor.listenTCP(8000, Site(root))
reactor.run()

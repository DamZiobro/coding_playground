#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

"""
echo_plugin.py - plugin of echo server
"""

from zope.interface import implements
from twisted.application.service import IServiceMaker
from twisted.application import internet
from twisted.plugin import IPlugin
from twisted.python import usage
from echoServer import EchoFactory

class Options(usage.Options):
    optParameters = [["port", "p", 8000, "The port number to listen on."]]
    class EchoServiceMaker(object):
        implements(IServiceMaker, IPlugin)
        tapname = "echoServer"
        description = "A TCP-based echo server."
        options = Options
        def makeService(self, options):
            """
            Construct a TCPServer from a factory defined in echoServer.py.
            """
            return internet.TCPServer(int(options["port"]), EchoFactory())
        serviceMaker = EchoServiceMaker()



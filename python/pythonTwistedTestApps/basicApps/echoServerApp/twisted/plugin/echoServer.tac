#!/usr/bin/python

from twisted.application import internet, service
from echoServer import EchoFactory

application = service.Application("echo")
echoService = internet.TCPServer(8000, EchoFactory())
echoService.setServiceParent(application)


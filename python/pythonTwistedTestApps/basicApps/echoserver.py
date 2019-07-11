#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
Echo server based on twisted
"""
from twisted.internet import protocol, reactor
class EchoProtocol(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        print "Data received: " + data

class EchoFactory(protocol.Factory):
    # replace buildProtocol() method with simpler idiom    
    protocol = EchoProtocol
    #def buildProtocol(self, addr):
        #return Echo()
    def connectionLost(self,reason):
        print "Connection lost. - reason: " + reason.getErrorMessage()

reactor.listenTCP(8000,EchoFactory())
reactor.run()

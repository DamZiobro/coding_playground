#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
Echo client based on twisted
"""
from twisted.internet import reactor, protocol

class EchoClientProtocol(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello, world!")

    def dataReceived(self, data):
        print "Server said:", data
        self.transport.write("Response: Hello world");
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    # replace buildProtocol() method with simpler idiom    
    protocol = EchoClientProtocol
    #def buildProtocol(self, addr):
        #return EchoClientProtocol()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - reason: " + reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost. - reason: " + reason.getErrorMessage()
        reactor.stop()

reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()

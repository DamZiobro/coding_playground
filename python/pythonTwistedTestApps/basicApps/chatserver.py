#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#

"""
This is example fo chatServer application written in Python Twisted library
"""

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from enum import Enum

class ChatState(Enum):
    REGISTER    = 1
    CHAT        = 2 

class ChatProtocol(LineReceiver):
    def __init__(self,factory):
        self.factory = factory
        self.name = None
        self.state = ChatState.REGISTER

    def connectionMade(self):
        self.sendLine("What's your name?: ")

    def connectionLost(self, reason):
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage("%s has left this chat" % (self.name))

    def lineReceived(self, line):
        if self.state == ChatState.REGISTER:
            self.handleRegisterState(line)
        else:
            self.handleChatState(line)

    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)

    def handleRegisterState(self, name):
        if name in self.factory.users:
            self.sendLine("Name taken, please choose another.")

        self.name = name
        self.state = ChatState.CHAT
        self.factory.users[name] = self

        self.broadcastMessage("%s has joined this chat." % (name))
        self.sendLine("Welcome, %s!" % (name))

    def handleChatState(self, message):
        self.broadcastMessage("[%s] => %s" % (self.name, message))

class ChatProtocolFactory(Factory):
    def __init__(self):
        self.users = {}
    def buildProtocol(self, addr):
        return ChatProtocol(self)

reactor.listenTCP(8000, ChatProtocolFactory())
reactor.run()


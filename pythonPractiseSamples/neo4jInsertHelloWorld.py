#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 damian <damian@C-DZ-E5500>
#
# Distributed under terms of the MIT license.

"""
Sample application to insert data into neo4j database
"""

from py2neo import Graph, Node, Relationship

if __name__ == "__main__":
    graph = Graph("http://localhost:7474", user="neo4j", password="damian")
    graph.delete_all()

    alice = Node("Person", name="alice", type="TopHighlightWidget")
    bob = Node("Person", name="bob", type="TopHighlightDataModel")

    alice_knows_bob = Relationship(alice, "knows", bob)
    graph.create(alice_knows_bob)

    alice2 = Node("Person", name="alice2", type="TopHighlightWidget")
    bob2 = Node("Person", name="bob2", type="TopHighlightDataModel")

    alice2_knows_bob2 = Relationship(alice2, "knows", bob2)
    graph.create(alice2_knows_bob2)

    bob3 = Node("Person", name="bob3", type="AnotherType")
    bob2_knows_bob3 = Relationship(bob2, "knows", bob3)
    graph.create(bob2_knows_bob3)


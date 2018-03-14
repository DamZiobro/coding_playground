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

    alice = Node("Person", name="0x75142F9C", type="GenericListTopHighlightWidget")
    bob = Node("Person", name="0x75142F9D", type="GenericListTopHighlightDataModel")

    alice_knows_bob = Relationship(alice, "mDataManager", bob)
    graph.create(alice_knows_bob)

    alice2 = Node("Person", name="0x85142F9C", type="GenericListTopHighlightWidget")
    bob2 = Node("Person", name="0x85142F9D", type="GenericListTopHighlightDataModel")

    alice2_knows_bob2 = Relationship(alice2, "mDataManager", bob2)
    graph.create(alice2_knows_bob2)


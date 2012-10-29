"""
Created on 29.10.2012

@author: aaa

Class node
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'aaa'


class node():

    def __init__(self, value):
        self.value = value
        self.neighbors = []
        pass

    def add_neighbor(self, neighbor):
        if (type(neighbor) == type(self)):
            self.neighbors.append(neighbor)
            if (self not in neighbor.neighbors): #undirected graph (bilateral or two-forked)
                neighbor.add_neighbor(self)
        else:
            print("param",neighbor,"have type",type(neighbor),", but need",type(self))
        pass

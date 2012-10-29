"""
Created on 29.10.2012

@author: aaa

"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'aaa'

import graph
from node import node

def main():
    n = node(17)
    n2 = node(21)
    n.add_neighbor(n2)


if __name__ == "__main__":
    main()
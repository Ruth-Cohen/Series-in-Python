# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:36:24 2018

@author: spanier
"""

def m(n):
    return sum(map(lambda n: float(n/(n+1)), range(1,n+1)))


def printm():
    n = int(input("enter a number: "))
    for i in range(1,n+1):
        print(i, m(i))
    return
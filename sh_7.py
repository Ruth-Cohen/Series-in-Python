# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:38:12 2018

@author: spanier
"""



def twinp(n):
    D = {}
    L = napa(n)
    for i in range(len(L)-2):
        if ((L[i + 1] - L[i]) == 2):
            D[L[i]] = L[i+1]
        if ((L[i + 2] - L[i]) == 2):
            D[L[i]] = L[i+2]
    return D

def napa(n):
    rishoni = [True]*n
    rishoni[0] = False
    for i in range(2,n):
        if rishoni[i]:
            for mlt in range(i*2,n,i):
                rishoni[mlt] = False
    res = []
    for i, item in enumerate(rishoni):
        if item:
            res.append(i)
    return res

def print_twinp():
    n = int(input("enter a number: "))
    D = twinp(n)
    for i in D.keys():
        print(i,D[i])
        
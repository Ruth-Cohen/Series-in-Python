# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:25:05 2018

@author: spanier
"""

import math

def pi(n):
    return 4*sum(map(lambda n: ((-1)**(n+1))/(2*n-1), range(1, n+1)))

def print_pi():
    n = int(input("enter a number: "))
    for i in range(1,n+1):
        print(i, pi(i))
    return
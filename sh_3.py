# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:49:37 2018

@author: spanier
"""

def  reverseNum1(n):
    st = str(abs(n))
    newStr = st[-1::-1]
    return int(newStr)

def  reverseNum2(n1):
    L = ' '
    n = abs(n1)
    while n > 0:
        s= str(int(n % 10))
        L += s
        n = int(n / 10)
    reversed(L)
    #print(L)
    return L

def reverseNum3():
    a = int(input("enter a number: "))
    print(reverseNum1(a))
    return
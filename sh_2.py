# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:26:04 2018

@author: spanier
"""
def sumDigits1(n1):
    return sum(map(int, list(str(abs(n1)))))


def sumDigits2(n1):
    L = []
    n = abs(n1)
    for i in range(n):
        s= int(n % 10)
        L.append(s)
        n = n / 10
    sum1=sum(L)
    return sum1

def sumDigits3():
    a = int(input("enter a number: "))
    print(sumDigits1(a))
    return
    
        
    
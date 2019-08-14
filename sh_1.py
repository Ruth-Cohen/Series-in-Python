# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def pentaNumRange(n1, n2):
    return list(map(lambda n : n*(3*n-1)/2, range (n1, n2)))

def print10():
    #L=[]
    num1 = int(input("enter 1 nums"))
    num2 = int(input("enter 1 nums"))
    def p10(n):
        for i in range(10):
            print(n, end=' ')
        
    #map(lambda  num1, num2: pentaNumRange(num1, num2))
    #L=pentaNumRange(num1, num2)
    return list(map(lambda n : p10(n), pentaNumRange(num1, num2)))
        
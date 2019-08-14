# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:19:39 2018

@author: spanier
"""

def isPalindrome(n):
    def  reverseNum1(n):
        st = str(abs(n))
        newStr = st[-1::-1]
        return int(newStr)
    if n == reverseNum1(n):
        print("It is a polindrom!! ")
        return True
    else:
        print("It is not a polindrom!! ")
        return False
        

    
    
def print_isPalindrome():
    n = int(input("please enter a number: "))
    return isPalindrome(n)
    
    
    
    
    
    

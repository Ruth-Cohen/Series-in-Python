# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:40:53 2018

@author: spanier
"""

from sh_1 import print10
from sh_2 import sumDigits3
from sh_3 import reverseNum3
from sh_4 import print_isPalindrome
from sh_5 import printm
from sh_6 import print_pi
from sh_7 import print_twinp
from sh_8 import print_add3dicts

D = dict([(1,print10),(2,sumDigits3),(3,reverseNum3),(4,print_isPalindrome)\
,(5,printm),(6,print_pi),(7,print_twinp),(8,print_add3dicts)])
print('0: exit\n1: ex1 penta numbers\n2: ex 2 sumDigits\n3:ex3 reverseNum\n4: ex4 isPalindrome\n5: ex5 m\n6: ex6 pi\n7: ex7 twin primes\n8: ex8 add3dicts\n')
while True:
	N = int(input('enter int val from the menue > '))
	if N == 0:
		break
	if N > 8 or N < 0:
		print('invalid input')
	else:
		D[N]()
		
from ex1 import mainEx1
from ex2 import mainEx2
from ex3 import mainEx3
from ex4 import mainEx4
from ex5 import mainEx5
from ex6 import mainEx6
from ex7 import mainEx7
from ex8 import mainEx8

D = dict([(1,mainEx1),(2,mainEx2),(3,mainEx3),(4,mainEx4)\
,(5,mainEx5),(6,mainEx6),(7,mainEx7),(8,mainEx8)])
print('0: exit\n1: ex1 penta numbers\n2: ex 2 sumDigits\n3:ex3 reverseNum\n4: ex4 isPalindrome\n5: ex5 m\n6: ex6 pi\n7: ex7 twin primes\n8: ex8 add3dicts\n')
while True:
	N = int(input('enter int val from the menue > '))
	if N == 0:
		break
	if N > 8 or N < 0:
		print('invalid input')
	else:
		D[N]()
		
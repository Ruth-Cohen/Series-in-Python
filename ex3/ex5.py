def m(n):
	func = lambda x: (x/ (x+1))
	def sumFunc(num,func):
		L = []
		for i in range(num):
			L.insert(0,func(i))
		return L
	return sum(sumFunc(n,func))
	
def mainEx5():
	L = int(input('> '))
	for i in range(L):
		print(str(i) , str(m(i)))
		

	
	
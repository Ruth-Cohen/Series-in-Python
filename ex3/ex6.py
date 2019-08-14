def pi(n):
	calcPi = lambda x:((-1)**(x+1))/(2*x-1)
	def sumFunc(num,func):
		L = []
		for i in range(1,num):
			L.insert(0,func(i))
		return L
	return 4*sum(sumFunc(n,calcPi))
	
def mainEx6():
	print(pi(int(input('> '))))
    
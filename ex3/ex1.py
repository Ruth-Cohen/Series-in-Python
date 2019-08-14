def pentaNumRange(n1,n2):
	L = []
	getPentaNum = lambda x: x*(3*x-1)/2
	for i in range(1,n2):
		if getPentaNum(i) in range(n1,n2):
			L.insert(i,i)
	return L


def mainEx1():
	n1 = int(input("enter n1> "))
	n2 = int(input("enter n2> "))
	if n1 >= n2:
		print("invalid input")
	print(pentaNumRange(n1,n2))
	
	
	
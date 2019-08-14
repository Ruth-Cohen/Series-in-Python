def reverseNum(n):
	return int(int(''.join(list(str(abs(n)))[-1::-1])) * n/abs(n))


def reverseNum2(n):
	def rever(num):
		L = []
		while num > 0:
			L.insert(0,str(int(num%10)))
			num = (num - num%10) / 10
		L.reverse()    
		return int(''.join(L))
	return int(rever(abs(n))* n/abs(n))

def mainEx3():
	print(reverseNum(int(input('enter num (positive or negative) > '))))
	print(reverseNum2(int(input('ver 2: enter num (positive or negative) > '))))



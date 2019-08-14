def sumDigits(n):
	return sum(list(map(int, list(str(abs(n))))))
	
	
def sumDigits2(n):
	def my_sum(num):
		L = []
		while num > 0:
			L.insert(0,int(num%10))
			num = (num - num%10) / 10
		return sum(L)
	return my_sum(abs(n))
def mainEx2():
	print(sumDigits(int(input('enter num (positive or negative) > '))))
	print(sumDigits2(int(input('ver 2: enter num (positive or negative) > '))))
	

from ex3 import reverseNum
def isPalindrome(n):
	return(reverseNum(n) == n)
	
def mainEx4():
	if isPalindrome(int(input('> '))):
		print("It is a palindrome !! ")
	else:
		print("It is not a palindrome ")
		

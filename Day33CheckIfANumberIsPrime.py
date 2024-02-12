#Write a test case for a function that checks if a number is prime
import math

def is_prime(n):
	if n<=1:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True

try:
	num=int(input("Enter a number greater than 0: "))
	if(is_prime(num)):
		print(num,"is a prime number.")
	else:
		print(num,"is not a prime number.")
except ValueError:
	print("Enter integers only.")
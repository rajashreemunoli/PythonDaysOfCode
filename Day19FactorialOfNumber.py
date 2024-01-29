#Write a function to calculate the factorial of a number
def factorial(num):
	if (num==1 or num==0):
		return 1
	else:
		return num*factorial(num-1)

try:
	number=int(input("Enter a number: "))
	print("Factorial of ",number," is: ",factorial(number))
except ValueError:
	print("Enter integer values only")
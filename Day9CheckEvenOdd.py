#Write a program to check if a number is even or odd
try:
	num=int(input("Enter number: "))
	x="Zero" if num==0 else "Even" if num%2==0 else "Odd"
	print(x)
except ValueError:
	print("Enter integers only")
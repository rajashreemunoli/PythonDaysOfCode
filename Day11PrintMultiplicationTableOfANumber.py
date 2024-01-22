#Write a program to print the multiplication table of a given number
def timestable(num):
	for i in range(1,11):
		print("%d X %d = %d" %(num,i,num*i))

try:
	number=int(input("Enter a number"))
	timestable(number)
except ValueError:
	print("Enter integers only")
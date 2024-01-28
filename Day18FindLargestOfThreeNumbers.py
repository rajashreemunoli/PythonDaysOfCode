#Create a program to find largest of three numbers
print("Enter 3 numbers:\n")

numbers=[]

while len(numbers)!=3:
	x=int(input())
	numbers.append(x)
	
print("Largest:",max(numbers))
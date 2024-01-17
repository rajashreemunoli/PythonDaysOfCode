#Write a program to check if a number is positive, negative, or zero

try:
	number=float(input("Enter a number: "))
	#Using the list comprehension method 
	x=["Positive" if number>0 else "Negative" if number<0 else "Zero"]
	print(x)

except ValueError:
	print("Enter numeric values only")

#Write a program to find the sum of all elements in a list

#Declare an empty list
list=[]

# 'try' part to handle the exception
try:
	print("Enter elements: ")

	#take inputs while we do not enter non-inetger types
	while True:
		x=float(input())
		list.append(x)

# When the code finds any non-integer type input, it will proceed to here
except:
	# Printing the list (assuming the input sequence has ended)
	print("List: ",list)



from functools import reduce
from operator import add

total=reduce(add, list)
print(total)
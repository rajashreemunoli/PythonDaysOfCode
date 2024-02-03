#Create a program to find the second-largest element in a list
def second_largest(lst1):
	lst2=list(set(lst1))
	lst2.sort()
	return lst2[-2]


print("Enter list elements one by one. Press enter when done.\n")
inputlist=[]
x=input()
try:
	while x!="":
		inputlist.append(float(x))
		x=input()

	print("Second largest element in list is:",second_largest(inputlist))
except:
	print('Enter numbers only')

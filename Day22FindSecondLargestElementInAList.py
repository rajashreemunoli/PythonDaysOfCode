#Create a program to find the second-largest element in a list

print("Enter list elements one by one. Press enter when done.\n")
inputlist=[]
x=input()
try:
	while x!="":
		inputlist.append(float(x))
		x=input()

	print("Second largest element in list is:",sorted(inputlist)[-2])
except:
	print('Enter numbers only')
#Create a function that calculates the average of a list of numbers
def avg_list(input_list):
	return sum(input_list)/len(input_list)

l1=input("Enter list of numbers separated by comma. Press enter when done:\n").split(',')
l1=[n for n in l1 if not n=='']
l2=list(map(float,l1))
print("Average of list: ",avg_list(l2))
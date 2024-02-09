#Create a function that finds the second smallest element in a list
def find_second_smallest(m):
	m.sort()
	print(m)
	return m[1]

print("Enter list elements separated by comma(,).\nPress enter when done:\n")
input_list=input().split(',')
print("Second smallest element in list is: ",find_second_smallest(input_list))
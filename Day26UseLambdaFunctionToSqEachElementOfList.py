#Create a program that uses a lambda function to square each element of a list
try:
	input_list=list(map(int,input("Enter list elements separated by comma:\n").split(',')))
	output_list=list(map(lambda x:x**2,input_list))
	print(output_list)
except ValueError:
	print("Enter integer values only. Do not type , after the last element")
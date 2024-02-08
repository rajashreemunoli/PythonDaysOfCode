# Python program to sort given array of string stored in a file

def sort_list(fp):
	
	# Open file for reading
	with open(fp, "r") as f:
		list1 = [line.strip() for line in f.readlines()]


	print("unsorted list: ",list1)

	# Sort the strings
	list1.sort()
	list2=[x for x in list1 if x.strip()]
 
	# Open the file for writing
	with open(fp, "w") as f:
		for line in list2:
			f.write(line + "\n")

	print("sorted list: ",list2)

 
# Print the sorted names
fname=input("Enter text file name:\n")
sort_list(fname)

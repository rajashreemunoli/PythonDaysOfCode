#Write a program to flatten a nested list
def flat_recursion(l):
	flist=[]
	for element in l:
		if type(element)==list:
			flist.extend(flat_recursion(element))
			#print(flist)
		else:
			flist.append(element)
			#print(flist)
	return flist

input_list=["WWC",["Python","Challenge"],[2024,[17,2,2024]],['a','b','c'],[1,2,3]]
#input_list=[1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

print("Nested List: ",input_list)
print("\nFlattened List: ",flat_recursion(input_list))
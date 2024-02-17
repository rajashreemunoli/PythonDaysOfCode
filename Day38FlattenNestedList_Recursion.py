#Write a program to flatten a nested list
def flat_recursion(l):
	flist=[]
	for element in l:
		if type(l)==list:
			flat_recursion(element)
		else:
			flist.append(element)
	return flist

input_list=["WWC",["Python","Challenge"],[2024,[17,2,2024]],['a','b','c'],[1,2,3]]

print("Nested List: ",input_list)
print("\nFlattened List: ",flat_recursion(input_list))
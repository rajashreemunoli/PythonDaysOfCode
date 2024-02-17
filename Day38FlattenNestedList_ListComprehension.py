#Write a program to flatten a nested list
def flat_listcompr(l):
	flist=[element for innerList in l for element in innerList]
	return flist

input_list=["WWC",["Python","Challenge"],[2024,[17,2,2024]],['a','b','c'],[1,2,3]]

print("Nested List: ",input_list)
print("\nFlattened List: ",flat_listcompr(input_list))
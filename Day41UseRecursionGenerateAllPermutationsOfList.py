#Write a program that uses recursion to generate all permutations of a list
def permute_list(lst,f=0):
	#base case
	if f>=len(lst):
		print(lst)

	for s in range(f,len(lst)):
		lst[f],lst[s]=lst[s],lst[f]
		permute_list(lst,f+1)
		lst[f],lst[s]=lst[s],lst[f]


permute_list([1,2,3])

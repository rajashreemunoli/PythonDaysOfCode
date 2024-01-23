#Write a program to shuffle the elements of a list randomly using Itertools.Permutations() Function
def shufflelist(input_list):
	import random
	import itertools
 
	permutations = list(itertools.permutations(input_list))
	shuffled_list = list(random.choice(permutations))
	print("Input List:",input_list)
	print("Shuffled List:", shuffled_list)

try:
	lst=[]
	print('Enter the list elements one by one. Press Enter when done\n')
	x=input()
	while x!="":
		lst.append(x)
		x=input()
	shufflelist(lst)

except ValueError:
	print("Try again")

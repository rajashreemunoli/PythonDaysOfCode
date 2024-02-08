#Create a function that generates a random number between a given range
def random_number(x,y):
	import random
	z=random.randrange(x,y)
	return z

a=int(input("Enter starting range: "))
b=int(input("Enter ending range: "))
print('\nRandom number: ',random_number(a,b))
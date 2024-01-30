#Write a function that takes a list of numbers and returns a new list containing only the even numbers
def is_integer(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
	else:
		float(num).is_integer()


def EvenList(lst1):
	lst2=[]
	for i in lst1:
		if is_integer(i)==True and int(i)%2==0:
			lst2.append(i)
	return lst2


print("Enter the list elements one by one.\nPress Enter when done.\n")
inputlist=[]
x=input()
while x!="":
	inputlist.append(x)
	x=input()

print("Input List: ",inputlist,"\nEven Numbers List: ",EvenList(inputlist))
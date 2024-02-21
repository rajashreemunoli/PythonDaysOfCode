#Write a program that uses a try-except block to handle division by zero
def avg_list(l):
	try:
		return sum(l)/len(l)
	except ZeroDivisionError:
		print("Empty lists are not acceptable.")
		


in_list=input("enter list of integers separated by commas:\n")
if in_list=="":
	listx=[]
else:
	listx=[int(x) for x in in_list.split(',')]
print(avg_list(listx))

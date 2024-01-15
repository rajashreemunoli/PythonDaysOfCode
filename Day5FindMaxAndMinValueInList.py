#Write a program to find the maximum and minimum values in a list
lst=[]

print("Enter list elements. \nType Enter when done.\n")

x=input()

while x!="":
	lst.append(x)
	x=input()
	
print("List: ",lst)
print("Min: ",min(lst,default="Invalid entry. Try Again."))
print("Max: ",max(lst,default="Invalid entry. Try Again."))
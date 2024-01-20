#Write a program to remove duplicates from a list
def remove_duplicates(dup):
	uniq=list(set(dup))
	return uniq


duplicate=[]
print("Enter list elements. Press Enter when done\n")
x=input()
while x!="":
	duplicate.append(x)
	x=input()

print("List of uniques:\n",remove_duplicates(duplicate))
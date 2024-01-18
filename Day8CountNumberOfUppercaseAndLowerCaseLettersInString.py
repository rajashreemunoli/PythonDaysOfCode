#Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it
def ulcount(s):
	d={"uppercase":0,"lowercase":0}
	for c in s:
		if c.isupper():
			d["uppercase"]+=1
		elif c.islower():
			d["lowercase"]+=1
		else:
			pass

	print("No. of Upper case characters: ", d["uppercase"])
	print("No. of Lower case characters: ", d["lowercase"])

x=input("Enter a string: ")
ulcount(x)
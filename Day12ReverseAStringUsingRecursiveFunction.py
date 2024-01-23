#Write a program to reverse a given string using recursive function
def reverse_string(input_string):
	if len(input_string)==0:
		return input_string
	else:
		return reverse_string(input_string[1:])+input_string[0]

string=str(input("Enter a string\n"))
print("Reversed String: ",reverse_string(string))
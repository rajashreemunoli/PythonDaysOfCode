#Create a program that capitalizes the first letter of each word in a sentence
import re
def replacement(match):
	return match.group(1)+match.group(2).upper()

def capitalize_first_letter(input_string):
	strlist=input_string.split()
	cap_string=""
	for word in strlist:
		if len(cap_string)>0:
			cap_string=cap_string+re.sub("(^|\s)(\S)",replacement,word)+" "
		else:
			cap_string=re.sub("(^|\s)(\S)",replacement,word)+" "

	return cap_string

string=input("Enter a sentence: ")
result=capitalize_first_letter(string)
print(result)

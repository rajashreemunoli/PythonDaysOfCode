#Write a program to remove vowels from a given string
def remove_vowels(str1):
	import re
	return re.sub('[aeiouAEIOU]',"",str1)


x=input('Enter the string: ')
print('String without vowels: ',remove_vowels(x))
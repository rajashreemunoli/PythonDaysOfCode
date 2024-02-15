#Write a Python program to check if two strings are anagrams
def is_anagram(str1,str2):
	list1=list(str1.lower())
	list2=list(str2.lower())
	list1.sort()
	list2.sort()
	return list1==list2
	

string1=input("Enter the first string: ")
string2=input("\nEnter the second string: ")
result=(is_anagram(string1,string2))
if result:
	print("anagrams")
else:
	print("not anagrams")

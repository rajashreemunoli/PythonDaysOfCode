#Write a function to count the number of vowels in a given string
#RegEx
import re

string = input("Enter string: ")

# using findall() function to match pattern
# Meta character '|' is used to depict 'either-or' sequence
vowels = re.findall("a|e|i|o|u", string)
print("Vowels found: ", vowels)
# count of number of vowels in the string
print("Number of vowels:", len(vowels))
#Write a program to count the occurrences of a specific character in a string
str1=input("Enter string:\n")
x=input("Enter the character to be counted: ")
count=str1.count(x)
print(x+" occurs "+str(count)+" times in "+str1)
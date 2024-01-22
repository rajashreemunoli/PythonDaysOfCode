#Write a program to reverse a given string using extended slice
def reverse(str1):
    str1 = str1[::-1]
    return str1
 
str_input=str(input("Enter a string\n"))
 
print("The original string is : ", end="")
print(str_input)
 
print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(str_input))
#Create a program that checks if a string is a palindrome
def is_palindrome(s):
    s=s.lower()
    l=len(s)
    if l<2:
        return True
    elif s[0]==s[l-1]:
        return is_palindrome(s[1:l-1])
    else:
        return False

str=input("enter a string: ")
if is_palindrome(str):
    print("Palindrome")
else:
    print("Not Palindrome")
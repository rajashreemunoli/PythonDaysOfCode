#Create a program that checks if a string is a palindrome
def is_palindrome(s):
    import math
    result=False
    s=s.lower()
    l=len(s)
    stop=math.floor(l/2)
    
    if l<2:
        result=True
        return result
    
    for i in range(0,stop):
        if s[i]==s[l-1-i]:
            result=True
            i+=1
        else:
            result=False
            break
    return result

str=input("enter a string: ")
if is_palindrome(str):
    print("Palindrome")
else:
    print("Not Palindrome")

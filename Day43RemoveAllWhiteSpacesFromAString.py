#Write a program that removes all whitespaces from a given string
def remove_ws(s):
    import re
    pattern=re.compile(r'\s+')
    res=re.sub(pattern,'',s)
    return res

in_str=input("Enter a string:\n")
try:
    print('String after removing white spaces:\n',remove_ws(in_str))
except ValueError:
    print('Enter strings only.')
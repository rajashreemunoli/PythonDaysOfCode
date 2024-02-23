#Write a program that reads an integer from the user and handles invalid inputs
try:
    x=int(input("enter an integer: "))
    print(x)
except:
    print("Enter integer values only")
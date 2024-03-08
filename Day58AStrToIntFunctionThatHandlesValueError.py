#Create a function that converts a string to an integer and handles ValueError
def str_to_int(s):
    try:
        num=int(s)
    except ValueError:
        num=''
        print("Invalid Entry. Enter integers only...")
    return num

str=input("Enter a number: ")
print(str_to_int(str))
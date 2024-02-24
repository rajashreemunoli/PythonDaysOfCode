#Write a function to check if a number is a prime number
def isprime(num):
    if num<=1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
    return True

try:
    x=int(input("Enter an integer value:"))
    if isprime(x)==True:
        print(f"{x} is a prime number")  
    else:
        print(f"{x} is not a prime number")
except:
    print("Invalid Input. Try again...")
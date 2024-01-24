#Write a program to print the first n numbers of a Fibonacci sequence
def PrintFib(n):
    fib=[]
    if n==1:
    	fib=[0]
    else:
        fib=[0,1]
        for i in range(1,n-1):
        	fib.append(fib[i]+fib[i-1])
    print("Fibonacci Sequence upto "+str(n)+" : ",fib)

try:
	N=int(input("Enter the number of Fibonacci numbers you want to see: "))
	PrintFib(N)
except ValueError:
	print("Enter integer values greater than 0 only")
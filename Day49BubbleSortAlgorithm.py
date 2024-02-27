#Create a program that implements the bubble sort algorithm
def bubble_sort(alist):
    iter=0
    swapped=True
    while swapped:
        swapped=False
        for i in range(0,len(alist)-iter-1):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
                swapped=True
        iter+=1
    return alist

try:
    input_list=[int(x) for x in input("Enter list of integers separated by comma:\n").split(',')]
    print("Sorted List:\n",bubble_sort(input_list))
except:
    print("invalid entry")
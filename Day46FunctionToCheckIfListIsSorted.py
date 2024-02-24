#Write a function to check if a given list is sorted
def checksorted(l):
    sl=l[:]
    sl.sort()
    print("Original List: ",l)
    print("\nSorted List: ",sl)
    if sl==l:
        return True
    else:
        return False

input_list=input("Enter list elements separated by comma:\n").split(',')
if checksorted(input_list):
    print("\nSorted")
else:
    print("\nNot Sorted")
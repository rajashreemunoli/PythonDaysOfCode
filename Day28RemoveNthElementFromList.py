#Create a program that removes the nth element from a list
original_list=input("Enter list elements separated by comma(,):\n").split(',')
position=int(input("Enter the position of the element to be eliminated: "))
original_list.pop(position-1)
print('List after elimination:\n', original_list)
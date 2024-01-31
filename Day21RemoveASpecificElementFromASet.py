#Create a program to remove a specific element from a set

set1={'Apple','Banana','Cherry','Fig','Grapes','Kiwi','Mango','Orange','Pear','Raspberry','Strawberry'}
print("List of Fruits:\n",set1)
x=input("\nEnter the fruit you want to remove: ")
print("Updated List of Fruits:\n",set1-{x.title()})
#Create a program that finds the intersection and union of two sets
set1=set((input("Enter values for 1st set separated by commas:").split(',')))
set2=set((input("Enter values for 2nd set separated by commas:").split(',')))
print("Union of set1 and set2:\n", set1|set2)
print("Intersection of set1 and set2:\n", set1&set2)
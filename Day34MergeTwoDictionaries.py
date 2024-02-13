#Write a Python program to merge two dictionaries
def merge_dicts(d1, d2):    
    merged_dict = dict(dict1.items() | dict2.items())
    return merged_dict
 

dict1 = {'A Tale of Two Cities':  'Charles Dickens', 'Le Petit Prince': 'Antoine de Saint-Exupéry','Harry Potter and the Philosophers Stone': 'J K Rowling'}
dict2 = {'And Then There Were None': 'Agatha Christie', 'Dream of the Red Chamber': 'Cao Xueqin','The Hobbit': 'J. R. R. Tolkien'}


# merge the two dictionaries using the Merge() function
dict3 = merge_dicts(dict1, dict2)
 
# print the merged dictionary
print(dict3)
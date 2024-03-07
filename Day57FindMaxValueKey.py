#Create a function that returns the key with the maximum value in a dictionary
def find_max_key(dict):
    max_key=max(dict,key=dict.get)
    return max_key

d={'Harry Potter':9.5,'Game of thrones':8.2,'Star Wars':8.9,'Avengers':9.9}
print(f'{find_max_key(d)} has the highest rating of {d[find_max_key(d)]}')
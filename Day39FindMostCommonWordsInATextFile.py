#Write a program to find the most common words in a text file
from collections import Counter
import re

f= open("To Kill a Mockingbird - Harper Lee.txt","r")
text =f.read()
#clean data
text=re.sub(r'[^\w\s]', '', text)

#to lower
text = text.lower()
#to list
ls = text.split()
#most_common = 20
top_20 = Counter(ls).most_common(20)
#loop all most_common 
for x in top_20:
  print(x)  
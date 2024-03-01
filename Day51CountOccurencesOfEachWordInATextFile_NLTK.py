#Create a program that counts the occurrences of each word in a text file
from nltk import corpus, FreqDist, word_tokenize
import re

f= open("test.txt","r")
text =f.read()


text=text.strip()

#to lower
text = text.lower()

#clean data
text=re.sub(r'[^\w\s]', '', text)

words = word_tokenize(text)
dist = FreqDist(words)

for k, v in dist.items():
    print(k, ':', v)
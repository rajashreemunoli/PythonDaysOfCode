import nltk
from nltk.corpus import wordnet
import random

def replace_word_with_synonym(text,word):
    synonyms=[]
    for s in wordnet.synsets(word):
        for l in s.lemmas():
            synonyms.append(l.name())
    
    new_text=text.replace(word,random.choice(list(set((synonyms)))))
    return new_text

sentence=input("Enter text:\n")
word_to_replace=input("\nEnter the word to be replaced with a synonym:\n")
print(f"\nText after replacing {word_to_replace} with a synonym:\n",replace_word_with_synonym(sentence,word_to_replace))
#Create a function to find all words in a sentence that start with a vowel
def find_words(sentence):
    #splits sentence into a list
    words_raw=sentence.split()
  
    #makes a new list with words without punctuations
    import string
    words=[word.strip(string.punctuation) for word in sentence.split() if word.strip(string.punctuation).isalnum()]
    vowels="aeiouAEIOU"
    #lists the words that start with vowels
    result=[word for word in words if word[0] in vowels]
    return result

s=input("enter a sentence: ")
print("words starting with vowels are:\n",find_words(s))
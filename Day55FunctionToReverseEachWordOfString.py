#Create a function that takes a string and returns the reverse of each word
def rev_words(sentence):
    words=sentence.split(' ')
    reversed=' '.join([word[::-1] for word in words])
    return reversed

s=input("enter a sentence: ")
print("sentence with reversed words:\n",rev_words(s))
#Write a function that counts the frequency of each word in a sentence
def frequency_counter(str):
	strlist=str.split()
	dictionary={}
	for word in strlist:
		if word[-1]==".":
			word=word[0:len(word)-1]

		if word in dictionary:
			dictionary[word]+=1
		else:
			dictionary.update({word:1})

	for everykey in dictionary:
		print(everykey+": ",dictionary[everykey])


sentence=input("Enter a string:\n")
frequency_counter(sentence)
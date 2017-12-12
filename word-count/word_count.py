import re

def word_count(phrase):
    	
	words = {}
	phrase = phrase.lower()
	rgx = re.compile("(\w[\w']*\w|\w)")
	phrase = rgx.findall(phrase)
	for word in phrase:	
		if not word in words:
			words.update({word: 1})
		else:
			words[word] += 1

	return words
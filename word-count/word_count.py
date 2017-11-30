import re
def word_count(phrase):
    new_phrase = phrase.lower().split(' ')
    d = {}
    for word in new_phrase:
        re.findall('r[a-z]', word)
        if d.get(word):
            d[word] +=1
        else:
            d.update({word:1})
    return d

def input_sanitizer(phrase):
    phrase = phrase.lower().split(' ')
    sanitized_list = []
    for word in phrase:
        xz = "".join(re.findall(r'[a-z]', word))
        sanitized_list += xz
    return sanitized_list

'''
'''TODO'''
be able to handle one string with no spaes, or with commas seperating words.
do a better job splitting, to avoid punctiations colons, etc
' logic' works, need to sanitize.

'''
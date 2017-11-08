def is_pangram(sentence):
    sentence_list = []
    for element in sentence:
        sentence_list += element.lower()
    for bit in alphabit_list():
        if bit not in sentence_list:
            return False
    return True






def alphabit_list():
    alphabit = 'abcdefghijklmnopqrstuvwxyz'
    alphabit = list(alphabit)
    return alphabit



# every letter atleas once
# repeating letters is okay.    
# to lower
#underscores ok
# spaes okay

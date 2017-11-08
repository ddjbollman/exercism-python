
#def is_isogram(string):
#    output = []
#    array = []
#    for letter in string:
#        if letter not in output:
#            output.append(letter)
#        for char in output:
#            if output.count(char)<= 1:
#                array.append(char)
#        if string == array      
#        else:
#            print('not isogram')
#            return False           




def is_isogram(string):
    output = []
    string = string.lower()
    for letter in string:
        # add hyphen exception
        if letter == '-' or letter == ' ':
            output.append(letter)
        # only add letters that are not already there (indicating that its not output)
        elif letter not in output:
            output.append(letter)
        else:
            return False
        # turn list back to a string, and compare to original.  if it matches. it means there was no repeating characters, minus '-'.
    newstring = "".join(output)
    if string == newstring:
        return True    
    else:
        return False


            
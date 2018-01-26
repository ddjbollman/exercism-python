def decode(string):
    if not string:
        return ''
    else:
        return 'thing'
# function will take 12W1B7C thing and turn it into raw. "Unpack"

def encode(string):
    encode_list = []
    sucessive_char_count = 0
    var_list = 0
    for char in string:
        # to run once.
        if var_list == 0:
            current_char = char
            var_list = 1
        if char == current_char:
            sucessive_char_count += 1
        else:
            encode_list.append(str(sucessive_char_count) + current_char)
            sucessive_char_count = 1
            var_list = 0
            
    return encode_list


    # this function will do the 12W1B7C thing
    # dictionaries might not work.
    #   this is because it will add matching values to existing keys
    # example 'AAABBAAAAAA' = 3A2B6A  but with the current implementation
    # it would come out as 9A2B.
    # how do i make order important


# using lists to keep state of chars and their amount
#def encode(string):

# original dictionary approach.
# need a dictionary
    '''
def encode(string):
    key_list = []
    d = {}
    if string:
        for char in string:
            # counters z +=1
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for key in d.keys():
            key_list += str(d[key]) + key
        return "".join(key_list)
    else:
        return ''
    '''


    # i need to do a for loop where once the char is diff than the previous one the previous char count is saved, and then another state keeping begins for the current char.





# original dictionary approach.
# need a dictionary

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
            if d[key] == 1:
                d[key] = ''
            # add if statement to check if the value is 1, if so ommit the value?
            # below takes dict, flips it and makes it an array
            # '2','A'
            key_list += str(d[key]) + key
            #array turns into a list
        return "".join(key_list)
    else:
        return ''
    

def decode(string):
    string = string






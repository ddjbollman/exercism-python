string = 'MMMMMMMMLLLLLLLGGGG'


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
            
print(encode_list)


for char in string:
    if var_list == 0:
        current_char = char
        print('current_char equals {}'.format(char))
        var_list = 1
    if char == current_char:
        sucessive_char_count +=1
        print('Inside if char equals current_char if statement;  current_char equals {} sucessive_char_count equals {}'.format(char, sucessive_char_count))
    else:
        print('Else statement trigered.')
        encode_list.append(str(sucessive_char_count) + current_char)
        print("encode_list is {}".format(encode_list))
        sucessive_char_count = 1
        print('sucessive char count var is at {}'.format(sucessive_char_count))
        var_list = 0



string = 'MMMMMMMMLLLLLLLGGGG'


encode_list = []
sucessive_char_count = 0
var_list = 0

for char in string:
    if var_list == 0:
        current_char = char
        print('current_char equals {}'.format(char))
        var_list = 1
    if char == current_char:
        sucessive_char_count +=1
        print('Inside if char equals current_char if statement;  current_char equals {} sucessive_char_count equals {}'.format(char, sucessive_char_count))
    else:
        print('Else statement trigered.')
        encode_list.append(str(sucessive_char_count) + current_char)
        print("encode_list is {}".format(encode_list))
        sucessive_char_count = 1
        print('sucessive char count var is at {}'.format(sucessive_char_count))
        var_list = 0
# Tom Croshaw - Project 1
# Problem 1 - PYTHON 3
# For this problem you will be writing a function that the supplied dictionary input_dict and operates on it.

import string

input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1,
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

vowels = 'aeiou'
consonents = string.ascii_lowercase

def modify_dict(dict):
    print ('Input Dictionary: ',input_dict)
    dict_new = {}
    # Iterate through the keys
    for key in dict:
        key = str(key)
        # For pairs where the key starts with a lowercase vowel, change the value to "vowel".
        if key[0].lower() in vowels:
            dict_new[key] = "vowel"
        # For pairs where the key starts with a lowercase consonant, change the value to "consonant".
        elif key[0].lower() in consonents and key[0].lower() not in vowels:
            dict_new[key] = "consonents"
        # else return nothing
        else:
            None
    print ('Output Dictionary: ',dict_new)
    return dict_new

assert (modify_dict(input_dict))

# Problem 1
import string

input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

def word(input_dict):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_dict = {}
    for k, v in input_dict.items():
        if type(k) == str:
            if k[0] in vowels:
                v = 'vowels'
            else:
                v = 'consonant'
            new_dict[k] = v 


    print(new_dict)
word(input_dict)
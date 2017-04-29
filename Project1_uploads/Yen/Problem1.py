

input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1,
            'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
             'CHARACTER':'C'}
             
vowels = list('aeiou')
consonants = list('bcdfghjklmnpqrstvwxyz')
def Problem1(dict):
    new_dict = {}
    print(dict)
    for key,value in dict.items():
        if type(key) == str and key[0].islower():
            if key[0] in vowels:
                value = 'vowel'
            else:
                value = 'consonant'
                new_dict[key] = value
    print(new_dict)
    return(new_dict)



Problem1(input_dict)

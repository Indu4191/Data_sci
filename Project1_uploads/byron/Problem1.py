# Review Problem 1
'''
For this problem you will be writing a function that the supplied dictionary input_dict and operates on it.

Define a function that:

    Accepts 1 argument, which will be a dictionary.
    Prints the dictionary.
    Iterates through the key:value pairs of the dictionary:
        For pairs where the key starts with a lowercase vowel, change the value to "vowel".
        For pairs where the key starts with a lowercase consonant, change the value to "consonant".
        Remove all other pairs from the dictionary.
    Prints the modified dictionary.
    Returns the modified dictionary.

Notes/Hints:

    string.ascii_lowercase is a string of all the lowercase letters in the alphabet. to use it you need to import string at the beginning of your script.
    You can check if a character is in a string with in. 
'''
print("Problem 1")

import string

# print out key/value pairs from dictionary
def print_dict(input_dict):
    for key, values in input_dict.items():
        print(key, ':', values)
        
# define a function that loops through the dictionary entries, removes and changes some as per requirements
def process_dict(input_dict):
    print("\nInput dictionary:")
    print_dict(input_dict)
    # setup vowels definition and empty dictionary to return new values
    vowels = ['a', 'e', 'i', 'o', 'u']
    # initialise empty dictionary
    new_dict = {}

    # loop through all dictionary values
    for keys,values in input_dict.items():
        #print("key =", keys, " value =", values)
        # only add entry if the key is a string and starts with a letter
        if type(keys) is str and keys[0].lower() in string.ascii_lowercase:
            # check if the character is a vowel, change value in dictionary
            if keys[0].lower() in vowels:
                new_dict[keys] = "vowel"
            # value is a consonant, change value in dictionary
            else:
                new_dict[keys] = "consonant"
    
    print("\nModified dictionary:")
    print_dict(new_dict)
    return new_dict

# setup input dictionary
input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

new_dict = process_dict(input_dict)
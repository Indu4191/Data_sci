# Review Problem 8
'''
Define three functions to "clean up" two dictionaries and merge them together.

Your first function, called string_intlist_cleaner should:

    Accept one argument which will be a dictionary.
    Iterate through the key:value pairs in the dictionary:
        If the key is not a string, remove the key:value pair from the dictionary.
        If the value is not a list, remove the key:value pair from the dictionary.
    Return the "cleaned" dictionary.

Your second function, called int_string_cleaner should:

    Accept one argument which will be a dictionary.
    Iterate through the key:value pairs in the dictionary:
        If the key is not an integer, remove the key:value pair from the dictionary.
        If the value is not a string, remove the key:value pair from the dictionary.
    Return the "cleaned" dictionary.

Your third function, called dict_cleaner should:

    Accept two arguments which will be dictionaries.
    Print the first dictionary.
    Print the second dictionary.
    Clean the first dictionary with string_intlist_cleaner() and assign to a variable.
    Clean the second dictionary with int_string_cleaner() and assign to a variable
    Combine the two cleaned dictionaries.
    Print the combined and cleaned dictionary.
    Return the combined and cleaned dictionary.
'''
print("Problem 8")

# print out key/value pairs from dictionary
def print_dict(input_dict):
    for key, values in input_dict.items():
        print(key, ':', values)

# If the key is a string and the value is a list, keep the entry
def string_intlist_cleaner(input_dict):
    new_input_dict = {}
    for keys,values in input_dict.items():
        if isinstance(keys, str) and isinstance(values, list):
            new_input_dict[keys] = values
    return new_input_dict

# If the key is an integer and the value is a string, keep the entry
def int_string_cleaner(input_dict):
    new_input_dict = {}
    for keys,values in input_dict.items():
        if isinstance(keys, int) and isinstance(values, str):
            new_input_dict[keys] = values
    return new_input_dict

def dict_cleaner(input_dict1, input_dict2):
    print("\nInput dictionary 1:")
    print_dict(input_dict1)
    print("\nInput dictionary 2:")
    print_dict(input_dict2)
        
    clean_dict1 = string_intlist_cleaner(input_dict1)
    clean_dict2 = int_string_cleaner(input_dict2)

    # combine the two cleaned dictionaries
    combined_dict = {**clean_dict1, **clean_dict2}
    print("\nCombined and cleaned dictionary")
    print_dict(combined_dict)
    
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

dict_cleaner(first_dict, second_dict)

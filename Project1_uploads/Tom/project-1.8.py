# Tom Croshaw - Project 1
# Problem 8 - PYTHON 3
# Define three functions to clean up two dictionaries and merge them together.

first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

def string_intlist_cleaner(dictInput):
    dict_clean_key = {k: v for k, v in dictInput.items() if type(k)==str} # Remove string keys and place in new dictionary
    dict_clean_value = {k: v for k, v in dict_clean_key.items() if type(v)==list} # Remove list values and place in new dictionary
    return dict_clean_value

def int_string_cleaner(dictInput2):
    dict_clean_key2 = {k: v for k, v in dictInput2.items() if type(k) == int} # Remove int keys and place in new dictionary
    dict_clean_value2 = {k: v for k, v in dict_clean_key2.items() if type(v) == str} # Remove string values and place in new dictionary
    return dict_clean_value2

def dict_cleaner(dict1, dict2) :
    print ('First Dictionary:',dict1)
    print ('Second Dictionary:',dict2)
    dict1_clean = string_intlist_cleaner(dict1) # Clean first dictionary
    dict2_clean = int_string_cleaner(dict2) # Clean second dictionary
    # Combine two cleaned dictionaries
    dict_final = dict1_clean.copy()
    dict_final.update(dict2_clean)
    print ('Cleaned Dictionary:',dict_final)
    return (dict_final)

assert (dict_cleaner(first_dict, second_dict))

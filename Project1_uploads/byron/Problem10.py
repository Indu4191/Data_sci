
# Review Problem 10
'''
Write a function that takes a tiered dictionary of dictionaries with arbitrary depth. Your function will iterate through the dictionary, printing out the contents.

Define a function that:

    Accepts at least one argument, the predefined dictionary.
    For each key:value pair, print out the key and the value.
    If the value is also a dictionary, do the same for that dictionary, but printing out the key:value pair with tabs equivalent to the current "depth" indicating what level we are on.
    Note: tab in strings is written as \t
    
    Example:

'key1' : 'value1'
'key2' :
    'key3' : 'value3'
    'key4' : 'value4'
    'key5' :
        'key6': 'value6'
'key7' : 'value7'
'''
print("Problem 10")

# define a function to print a dictionary formatted with tab indentations for readability
def dictionary_print_with_tabs(input_dict, num_tabs):
    # add 1 to the number of tabs to print
    num_tabs += 1

    # loop through all dictionary values
    for keys,values in input_dict.items():
        # print number of tabs based on the depth of the dictionary level
        print('\t' * num_tabs, end="")

        if isinstance(values, dict):
            # if we're on a dictionary print the keys only and call the function recursively
            # to handle whatever is in the values
            print(keys, ':')
            dictionary_print_with_tabs(values, num_tabs)
        else:
            # not on a dictionary so print the keys and whatever is in values
            print(keys, ':', values)

tiered_dict = {'T1.1':'V1.1', 
               'T1.2':'V1.2',
               'T1.3':{'T2.1':'V2.1',
                       'T2.2':['V2.2.1','V2.2.2'],
                       'T2.3':{'T3.1':['V3.1.1','V3.1.2'],
                               'T3.2':'V3.2',
                               'T3.3':'V3.3'}},
               'T1.4':{'T2.4':{'T3.4':{'T4.1':'V4.1',
                                       'T4.2':'V4.2'},
                               'T3.5':{'T4.3':'V4.3'}},
                       'T2.5':['V2.3.1','V2.3.2']},
               }

# pass tiered_dict and pass -1 for num_tabs so first level of dictionary is printed without tab indentation
dictionary_print_with_tabs(tiered_dict, -1)

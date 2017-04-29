# Tom Croshaw - Project 1
# Problem 10 - PYTHON 2
# Write a function that takes a tiered dictionary of dictionaries with arbitrary depth. Your function will iterate through the dictionary, printing out the contents.

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

def nested_dict(dict_input, indent=0):
    if isinstance(dict_input, dict): #Checks if the input is a dictionary
        for key, value in dict_input.iteritems(): #if a dictionary, iterate through the items...
            print '\t' * indent + key, value # ...print an indented key, value pair
            if isinstance(value, dict): # Returns true if value is a subclass of dict
                nested_dict(value, indent+1) #Increase the indent value
            else:
                pass

print nested_dict(tiered_dict)

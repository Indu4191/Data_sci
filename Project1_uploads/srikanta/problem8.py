#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:13:56 2017

@author: srikanta
"""

###################################################################
#PROBLEM 8
###################################################################
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

#Define three functions to "clean up" two dictionaries and merge them together.
#Your first function, called string_intlist_cleaner should:
#Accept one argument which will be a dictionary.
#Iterate through the key:value pairs in the dictionary:
#If the key is not a string, remove the key:value pair from the dictionary.
#If the value is not a list, remove the key:value pair from the dictionary.
#Return the "cleaned" dictionary.

def string_intlist_cleaner(dict_to_clean):
    cleaned_first = {}
    for k,v in dict_to_clean.items():
        if isinstance(k,str) and isinstance(v,list):
            cleaned_first[k] = v
    return cleaned_first
#Your second function, called int_string_cleaner should:
#Accept one argument which will be a dictionary.
#Iterate through the key:value pairs in the dictionary:
#If the key is not an integer, remove the key:value pair from the dictionary.
#If the value is not a string, remove the key:value pair from the dictionary.
#Return the "cleaned" dictionary.

def int_string_cleaner(dict_to_clean):
    cleaned_second = {}
    for k,v in dict_to_clean.items():
        if isinstance(k,int) and isinstance(v,str):
            cleaned_second[k] = v
    return cleaned_second
#Your third function, called dict_cleaner should:
#Accept two arguments which will be dictionaries.
#Print the first dictionary.
#Print the second dictionary.
#Clean the first dictionary with string_intlist_cleaner() and assign to a variable.
#Clean the second dictionary with int_string_cleaner() and assign to a variable
#Combine the two cleaned dictionaries.
#Print the combined and cleaned dictionary.
#Return the combined and cleaned dictionary.
def dict_cleaner(dict_to_clean_first, dict_to_clean_second):
    cleaned_first = string_intlist_cleaner(first_dict)
    #print (cleaned_first)
    cleaned_second = int_string_cleaner(second_dict)
    #print (cleaned_second)
    return dict(list(cleaned_first.items()) + list(cleaned_second.items()))

print (dict_cleaner(first_dict,second_dict))
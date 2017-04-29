#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------
Created on Fri Mar 24 10:20:57 2017

@author: srikanta
"""
#####################################################################
#PROBLEM 1
#####################################################################

import string


input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

alphabet = list(string.ascii_lowercase)
vowels = list('aeiou')

new_dict = {}
def vowelandconsonant(inputdict):
    for k,v in input_dict.items():
        if isinstance(k,str):
            if k[0] in vowels:
                new_dict[k]="vowel"
            elif k[0] in alphabet:
                new_dict[k] = "consonant"

vowelandconsonant(input_dict)
print (new_dict)
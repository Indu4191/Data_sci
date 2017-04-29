#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:04:36 2017

@author: srikanta
"""

###################################################################
#PROBLEM 2
###################################################################
test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

def division (inputdict, rem=[2]):
    final_dict = {}
    s = []
    for k,v in test_dict.items():
        for val in v:
            for r in rem:
                s.append(int(val) % r)
                #print (val, r, int(val) % r)
            final_dict[val] = s
            s = []
    return final_dict
print ("New Dictionary with default set of Remainder")
print (division(test_dict))
print ("\n")
print ("New Dictionary with full set of Remainder")
print (division(test_dict, optional_remainder))

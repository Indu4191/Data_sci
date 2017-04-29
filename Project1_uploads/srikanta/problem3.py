#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:06:38 2017

@author: srikanta
"""
###################################################################
#PROBLEM 3
###################################################################
list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]

print (list1)
print (list2)

def func(l1,l2):
    i = 0
    x = 0
    while x<= 300:
        print ('iteration: ' + str(i + 1))
        i += 1
        for val1, val2 in list(zip(l1,l2)):
            x = val1 * val2
            print (val1, val2, x)
            if x >300:
                break
        if x<= 300:
            l1 = [2*a for a in l1]
            l2 = [2*a for a in l2]
        else:
            break
        
func(list1,list2)

            
#        
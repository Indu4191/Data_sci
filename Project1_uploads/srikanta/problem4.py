#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:49:28 2017

@author: srikanta
"""

###################################################################
#PROBLEM 4
###################################################################


def statfunc(a,numberset):
    print (a)
    print ("Mean of numbers:  " + str(sum(numberset)/len(numberset)))
    numberset.sort()
    print (numberset)
    if len(numberset) % 2 == 0:
        median  = numberset[int(len(numberset)/2)]
    else:
        median = (numberset[int(len(numberset)/2)] + numberset[int(len(numberset)/2) +1])/2
    print ("Median of numbers:  " + str(median))
    
for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    statfunc(i,numbers)    



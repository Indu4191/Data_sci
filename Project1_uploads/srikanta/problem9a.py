#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:54:55 2017

@author: srikanta
"""

###################################################################
#PROBLEM 9a
###################################################################

# Change this filepath to point to the location of the .csv on your own computer:
filepath = '/home/srikanta/DS/Project1/pokedex_basic.csv'

# Code to read in pokedex info
raw_pd = ''
lst_final=[]
with open(filepath, 'r') as f:
    raw_pd = f.read()
   
    for l in raw_pd.splitlines():
        lst_temp = l.split(",")
        lst = []
        for x in lst_temp:
            w = x.replace('"','')
            if w.isdigit():
#                print (itm)
                lst.append(float(w))
            elif w == '':
                lst.append(-1)
            else:
                lst.append(w)
        lst_final.append(lst)
print(lst_final)
f.close()

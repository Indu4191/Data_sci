#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:00:27 2017

@author: srikanta
"""

###################################################################
#PROBLEM 5
###################################################################

from scipy.stats.stats import pearsonr
import numpy as np

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def pcorrcoeff(x,y):
    print (x)
    print (y)
    print ("")
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    
    x_deviation = [a - x_mean for a in x]
    y_deviation = [a - y_mean for a in y]
    
    x_deviation_sq = [a ** 2 for a in x_deviation]
    y_deviation_sq = [a ** 2 for a in y_deviation]
    
    sqrt_x_deviation_sq = sum(x_deviation_sq) ** 0.5
    sqrt_y_deviation_sq = sum(y_deviation_sq) ** 0.5
    
    xy_deviation = []
    for xval,yval in zip (x_deviation, y_deviation):
        xy_deviation.append(xval * yval)
    
    person_r = sum(xy_deviation)/(sqrt_x_deviation_sq * sqrt_y_deviation_sq)
    #print calculated pearson coeff
    print ("Calculated Pearson coeff:")
    print (person_r)

# call pearson coeff function
pcorrcoeff(X,Y)
# print numpy pearson coeff
print ("Numpy Pearson coeff:")
print (np.corrcoef(X,Y)[0,1])
# print scipy pearson coeff
print ("Scipy Pearson coeff:")
print (pearsonr(X, Y))

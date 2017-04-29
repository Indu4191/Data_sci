#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 22:40:49 2017

@author: srikanta
"""

###################################################################
#PROBLEM 6
###################################################################

from scipy.stats.stats import rankdata
from scipy.stats.stats import spearmanr
import numpy as np

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def spearmancoeff(x,y):
    #Accept the provided lists of numbers defined for problem 5, X and Y.
    print (x)
    print (y)
    print ("")
    #Calculate the rank of the numbers in the X and Y lists. The rank is a number that defines what index position each number would be if the list were in order.
        #For example: say list1 = [5,2,0,9,-5], then list1_rank = [3,2,1,4,0]
        #Calculating the rank is not trivial. You can use the rankdata() function from scipy.stats on a list to get the ranks of the numbers.
        #Assign the rank of list X to variable X_rank and list Y to variable Y_rank.
    x_rank = rankdata(x)
    y_rank = rankdata(y)
    
    #Manually calculate the covariance between X_rank and Y_rank as XY_rank_cov:
        #Calculate X_mean: the mean of X_rank using np.mean().
        #Calculate Y_mean: the mean of Y_rank using np.mean().
        #Calculate X_deviation: subtract X_mean from each element of X_rank.
        #Calculate Y_deviation: subtract Y_mean from each element of Y_rank.
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    x_deviation = [a - x_mean for a in x_rank]
    y_deviation = [a - y_mean for a in y_rank]

        #Calculate XY_d: multiply X_deviation with Y_deviation, element by element. You can use pythons zip() function to iterate across lists at the same time:
        #for xd, yd in zip(X_deviation, Y_deviation):
    xy_deviation = []
    for xval,yval in zip (x_deviation, y_deviation):
        xy_deviation.append(xval * yval)
        #Calculate sum_XY_d: the sum of the elements in XY_d with np.sum.
    sum_xy_deviation = np.sum(xy_deviation) 
    
        #Calculate XY_rank_cov: divide sum_XY_d by len(XY_d).
    xy_rank_cov = sum_xy_deviation/len(xy_deviation)
    #Calculate the standard deviations X_rank_std and Y_rank_std of the X_rank and Y_rank lists. You can use np.std().
    
    x_rank_std = np.std(x_rank)
    y_rank_std = np.std(y_rank)
    
    #Calculate the spearman rank correlation coefficient as XY_spearman: divide XY_rank_cov by (X_rank_std * Y_rank_std).
    xy_spearman = xy_rank_cov/(x_rank_std * y_rank_std)
    #Print XY_spearman.
    print ("Calculated Spearman coeff:")
    print (xy_spearman)

# call spearman coeff function
spearmancoeff(X,Y)

#Compare your value to the scipy function for spearman: print out spearmanr(X, Y).
print ("Scipy Spearman coeff:")
print (spearmanr(X, Y))

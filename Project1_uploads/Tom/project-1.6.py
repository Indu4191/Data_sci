# Tom Croshaw - Project 1
# Problem 6 - PYTHON 3
# For this problem you will be defining a function that calculates the spearman rank correlation coefficient between two lists. Spearman's rho is a measure of how related two sets of numbers are.

import numpy as np
import scipy.stats as stats

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def SRCC(list1, list2):
    # Calculate the rank of the numbers in the X and Y lists.
    x_rank = stats.rankdata(list1)
    y_rank = stats.rankdata(list2)
    # Manually calculate the covariance between X_rank and Y_rank as XY_rank_cov
    x_mean = np.mean(x_rank)
    y_mean = np.mean(y_rank)
    X_deviation = [x - x_mean for x in x_rank]
    Y_deviation = [y - y_mean for y in y_rank]
    XY_d = [xd * yd for xd, yd in zip(X_deviation, Y_deviation)]
    sum_XY_d = np.sum(XY_d)
    XY_rank_cov = sum_XY_d / len(XY_d)
    # Calculate the standard deviations X_rank_std and Y_rank_std
    X_rank_std = np.std(x_rank)
    Y_rank_std = np.std(y_rank)
    # Calculate the spearman rank correlation coefficient
    XY_spearman = XY_rank_cov / (X_rank_std * Y_rank_std)
    return XY_spearman

print ('SRCC:',SRCC(X,Y))
# Check against scipy function
print ('Scipy Check:',stats.spearmanr(X,Y))

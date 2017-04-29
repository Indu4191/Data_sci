# Tom Croshaw - Project 1
# Problem 5 - RUN IN PYTHON 2
# Define a function that calculates the pearson correlation coefficient between two lists of numbers.

import numpy as np

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def pearson_coef(list1, list2):
    print 'Length of X:',len(list1)
    print 'Length of Y:',len(list2)
    # Calculate the pearson correlation coefficient between the two lists and assign the value to variable pearson_r
    X_deviation = map(lambda x: x - np.mean(list1), list1) # map() applies an action to every member of an iterable: lambda creates the mean subtractor function
    Y_deviation = map(lambda x: x - np.mean(list2), list2)
    sqrt_X_deviation_sq = np.sqrt(sum(x**2 for x in X_deviation))
    sqrt_Y_deviation_sq = np.sqrt(sum(x**2 for x in Y_deviation))
    sum_XY_deviation =  sum(x_d * y_d for x_d, y_d in zip(X_deviation, Y_deviation))
    pearson_r = float(sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq))
    print 'Pearson Coef: ', pearson_r
    return pearson_r

assert pearson_coef(X,Y)

# Check against numpy function
print 'Numpy Check: ',np.corrcoef(X, Y)[0,1]

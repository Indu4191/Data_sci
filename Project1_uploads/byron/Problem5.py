# Review Problem 5
'''
Define a function that calculates the pearson correlation coefficient between two lists of numbers.

Your function will:

    Accept two arguments (the provided lists X and Y).
    Print the length of X and Y like so:

    Length of X: 40
      Length of Y: 40

    Calculate the pearson correlation coefficient between the two lists and assign the value to variable pearson_r.
        Create a variable X_deviation that is each element of X minus the mean of X.
        Create a variable Y_deviation that is each element of Y minus the mean of Y.
        Create a variable sqrt_X_deviation_sq that is the square root of the sum of the square of each element of X_deviation.
        Create a variable sqrt_Y_deviation_sq that is the same thing you just did but for Y_deviation.
        Create a variable sum_XY_deviation that is the sum of each element of X_deviation and Y_deviation multiplied by each other, in order. You can use the zip() function to iterate through two lists at the same time:

        for x_d, y_d in zip(X_deviation, Y_deviation):

        pearson_r is equal to sum_XY_deviation divided by (sqrt_X_deviation_sq * sqrt_Y_deviation_sq).
    Print pearson_r.
    Check if it is the same as numpy's correlation function. Print np.corrcoef(X, Y)[0,1]
'''
print("Problem 5")

import numpy

# define a function that calculates the pearson correlation coefficient between two lists of numbers
def calculate_pearson(X, Y):
    print("Length of X:", len(X))
    print("Length of Y:", len(Y))
    
    # calculate the X and Y deviations from the mean
    meanX = numpy.mean(X)
    X_deviation = [(x - meanX) for x in X]
    meanY = numpy.mean(Y)
    Y_deviation = [(y - meanY) for y in Y]    
    #print(X_deviation, Y_deviation)
    
    # calculate the square root of the sum of the square of each element of X_deviation and Y_deviation
    sqrt_X_deviation_sq = numpy.sqrt(sum([x ** 2 for x in X_deviation]))
    sqrt_Y_deviation_sq = numpy.sqrt(sum([y ** 2 for y in Y_deviation]))
    #print(sqrt_X_deviation_sq, sqrt_Y_deviation_sq)

    # calculate the sum of each element of X_deviation and Y_deviation multiplied by each other
    sum_XY_deviation = 0
    for value1, value2 in zip(X_deviation, Y_deviation):
        sum_XY_deviation += value1 * value2
    #print(sum_XY_deviation)
    
    #calculate pearson coefficient
    pearson_r = sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)
    print("pearson_r =", pearson_r)
    print("numpy.corrcoef(X, Y)[0,1] =", numpy.corrcoef(X, Y)[0,1])
    
X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

calculate_pearson(X, Y)

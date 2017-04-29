import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## A. Explore the Mad Men Cast Data

#1. Load the Mad Men cast show data
cast_data_csv = ('/Users/User/Desktop/Data Science Immersive/Week 2/datasets/mad-men-cast-show-data.csv')

cast_data_csv = pd.read_csv('/Users/User/Desktop/Data Science Immersive/Week 2/datasets/mad-men-cast-show-data.csv', encoding='ISO-8859-1')
#2. Print the head and tail 
#print(cast_data_csv.head())
#print(cast_data_csv.tail())

#3. Print the column
#print(cast_data_csv.columns)

# Problem 5 - Pearson Correlation Coefficient
import numpy as np

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

## To print the length of X and Y
def two_functions(X, Y):
        return len(X)
        return len(Y)

#print(len(X))
#print(len(Y))

## To calculate the pearson correlation coeff
pearson_r = np.cov(X, Y)
#print(pearson_r)

## Create variable x_deviation
X_mean = np.mean(X)
#print(X_mean)
#Answer: 20.49
X_deviation = []
X[:] = [a - X_mean for a in X]
X_deviation = X[:]
#print(X_deviation)

## Create variable Y_deviation
Y_mean = np.mean(Y)
#print(Y_mean)
#Answer: 20.15
Y_deviation = []
Y[:] = [b - Y_mean for b in Y]
Y_deviation = Y[:]
#print(Y_deviation)

## Create sqrt_X_deviation_sq
sqrt_X_deviation_sq = np.sqrt(np.sum(np.square(X_deviation)))
#print(sqrt_X_deviation_sq) 
#Answer: 80.2901986546

## Create sqrt_Y_deviation_sq
sqrt_Y_deviation_sq = np.sqrt(np.sum(np.square(Y_deviation)))
#print(sqrt_Y_deviation_sq)
#Answer: 96.88

## Create sum_XY_deviation
sum_XY_deviation = np.sum([(a*b) for a,b in zip(X_deviation, Y_deviation)])
#print(sum_XY_deviation)

## Formula
pearson_r = sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)
print(pearson_r)
# Answer: 0.659990523006

## To check for function
check_function = np.corrcoef(X, Y)[0, 1]
print(check_function)

# Answer: 0.659990523006
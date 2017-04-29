# Problem 6 - Spearman Rank Correlation Coefficient
from scipy.stats import rankdata
from scipy.stats import spearmanr
import numpy as np

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def two_functions(X, Y):
    return X
    return Y
#print(X)
#print(Y)
 

## To calculate the rank of the nos in the X and Y lists
X_rank = rankdata(X, method = 'ordinal')
print(X_rank)

Y_rank = rankdata(Y, method = 'ordinal')
print(Y_rank)

## Calculate the covariance of X_rank and Y_rank
# XY_rank_cov = np.cov(X_rank,Y_rank)
# print(XY_rank_cov)

## 1. Calculate the mean of X_rank
X_mean = np.mean(X_rank)
#print(X_mean)
#Answer : 20.5

##2. Calculate the mean of Y_rank
Y_mean = np.mean(Y_rank)
#print(Y_mean)
#Answer : 20.5

##3. Subtract X_mean from each element of X_rank
X_deviation = []
X[:] = [a - X_mean for a in X_rank]
X_deviation = X[:]
#print(X_deviation)

##4. Subtract Y_mean from each element of Y_rank
Y_deviation = []
Y[:] = [b - Y_mean for b in Y_rank]
Y_deviation = Y[:]
#print(Y_deviation)

##5. Multiply X_deviation with Y_deviation 
XY_d = [a*b for a,b in zip(X_deviation, Y_deviation)]
#print(XY_d)

##6. Sum of the elements in XY_d
sum_XY_d = np.sum(XY_d)
#print(sum_XY_d)

##7. Divide sum_XY_d by len(XY_d)
XY_rank_cov = sum_XY_d / len(XY_d)
#print(XY_rank_cov)

## Calculate the standard deviations of X_rank and Y_rank
X_rank_std = np.std(X_rank)
#print(X_rank_std)

Y_rank_std = np.std(Y_rank)
#print(Y_rank_std)

## Calculate the spearman rank correlation coefficient
XY_spearman = XY_rank_cov / (X_rank_std * Y_rank_std)
print(XY_spearman)
#Answer: 0.72138836773

## Compare value to the Scipy function
print(spearmanr(X, Y))
#Answer: 0.72138836773


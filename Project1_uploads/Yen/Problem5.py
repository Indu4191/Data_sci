import string
import time
import math
import numpy as np
import pandas as pd
import csv
from scipy import stats

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def Problem5(x,y):
   print('Length of X: '+ str(len(x)))
   print('Length of Y: '+ str(len(y)))

   mean_X = np.mean(x)
   mean_Y = np.mean(y)
   X_deviation = []
   Y_deviation = []

   for i in x:
       X_deviation.append(i-mean_X)
   for j in y:
       Y_deviation.append(j-mean_Y)

   square_X = [np.square(a) for a in X_deviation]
   square_Y = [np.square(b) for b in Y_deviation]

   sum_sq_X = sum(square_X)
   sum_sq_Y = sum(square_Y)

   sqrt_X_deviation_sq = np.sqrt(sum_sq_X)
   sqrt_Y_deviation_sq = np.sqrt(sum_sq_Y)

   XY_deviation = []

   for x_d, y_d in zip(X_deviation, Y_deviation):
       XY_deviation.append(x_d*y_d)

   sum_XY_deviation = sum(XY_deviation)

   pearson_r = sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)

   print(pearson_r)

Problem5(X,Y)
print(np.corrcoef(X,Y)[0,1])

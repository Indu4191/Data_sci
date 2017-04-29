import string
import time
import math
import numpy as np
import pandas as pd
import csv
from scipy import stats


def Problem4(i, numbers):
    print(type(i))
    #calculate mean of numbers:
    mean_numbers = sum(numbers)/len(numbers)
    #calculate median
    size = len(numbers)
    if size % 2 == 0:
        median_numbers = (numbers[size/2] + ((numbers[size]/2))+1)/2
    else:
        median_numbers = numbers[int((size/2)+0.5)]

    print('mean: ' + str(mean_numbers))
    print('median: ' + str(median_numbers))

 # Provided for loop for i and numbers:

for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]

#Call your function here using i and numbers:
Problem4(i, numbers)

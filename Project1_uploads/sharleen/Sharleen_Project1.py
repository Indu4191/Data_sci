#Project 1 Week 2
#sharleenies
#Submitted 28th March 2017

import numpy as np
import string
from scipy import stats
import csv
import pandas as pd

#Problem 1
input_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1,
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

def print_dict(dict):
    x = {}
    for k,v in dict.items():
        if type(k) == str and k[0].islower():
            if k[0] in ['a','e','i','o','u']:
                v = 'vowel'
            else:
                v = 'consonant'
            x[k] = v
    print(dict)
    print (x)

print_dict(input_dict)


#Problem 2
test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

def list_remainder(dict,optional_remainder):
    final_output_d = {}
    if len(optional_remainder) == 0:
        optional_remainder.append(2)
    for k,v in dict.items():
        new_dict = {}
        for x in v:
            remainder = [float(x % r) for r in optional_remainder]
            new_dict[x] = remainder
        # print (new_dict)
        # print (remainder)
        final_output_d[k] = new_dict


    print (final_output_d)
list_remainder(test_dict,optional_remainder)

# Problem 3
list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]

def multiply_until(list1,list2):
    iteration = 0
    print (list1)
    print (list2)
    while len(list1) ==4:
        for value1, value2 in zip(list1, list2):
            multiplied = value1 * value2
            iteration += 1
            print ("Iteration " + str(iteration))
            print (multiplied)
            # print (list1)
            # print (list2)
        if multiplied < 300:
            list1 = [x*2 for x in list1]
            list2 = [y*2 for y in list2]
        else:
            print ('Function Complete')
            break

multiply_until(list1,list2)


# Problem 4

for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]

def function(i,numbers):
    lst = sorted(numbers)
    length = len(lst)
    center = length // 2
    print("i: "+ str(i))
    print ("Mean: " + str(float(sum(numbers)) / max(len(numbers), 1)))
    if len(lst) < 1:
        print('None')
    elif len(lst) % 2 == 0:
        print ("Median: " + str(sum(lst[center - 1: center + 1]) / 2.0))
    else:
        print ("Median: " + str(lst[center]))
function(i,numbers)

# Problem 5

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def pearson(X,Y):
    print ("Length of X: " + str(len(X)))
    print ("Length of Y: " + str(len(Y)))
    numpy_pearson_r = np.corrcoef(X,Y)[0, 1]
    print ('Numpy Pearson_r: ' + str(numpy_pearson_r))

    X_deviation = [x - np.mean(X) for x in X]
    sum_squared1 = 0
    for a in X_deviation:
        sum_squared1 += np.square(a)
        sqrt_X_deviation_sq = np.sqrt(sum_squared1)

    Y_deviation = [y - np.mean(Y) for y in Y]
    sum_squared2 = 0
    for b in Y_deviation:
        sum_squared2 += np.square(b)
        sqrt_Y_deviation_sq = np.sqrt(sum_squared2)

    sum_XY_deviation = 0
    for x_d, y_d in zip(X_deviation, Y_deviation):
        sum_XY_deviation += x_d * y_d

    pearson_r = sum_XY_deviation / (sqrt_X_deviation_sq * sqrt_Y_deviation_sq)
    print ('My calculated pearson_r: ' + str(pearson_r))

pearson(X,Y)


# Problem 6
X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def spearman(X,Y):
    X_rank = stats.rankdata(X)
    Y_rank = stats.rankdata(Y)

    X_mean = np.mean(X_rank)
        # print (X_mean)
    Y_mean = np.mean(Y_rank)
        # print (Y_mean)
    X_deviation = [a - X_mean for a in X_rank]
    Y_deviation = [b - Y_mean for b in Y_rank]

    XY_d = [e * f for e,f in zip(X_deviation, Y_deviation)]
        # print (XY_d)
    sum_XY_d = np.sum(XY_d)
    XY_rank_cov = sum_XY_d / len(XY_d)

    X_rank_std = np.std(X_rank)
    Y_rank_std = np.std(Y_rank)

    XY_spearman = XY_rank_cov / (X_rank_std * Y_rank_std)
    print ('My XY_spearman: ' + str(XY_spearman))

spearman(X,Y)
print ('Scipy function spearman: ' + str(stats.spearmanr(X,Y)[0]))


# Problem 7
predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def RMSE(true_values, predictions):
    errors = [b - a for a,b in zip(true_values, predictions)]
    # print (errors)
    sq_errors = [np.square(x) for x in errors]
    avg_sq_error = np.mean(sq_errors)
    rmse = np.sqrt(avg_sq_error)
    print (rmse)
RMSE(true_values, predictions)


# Problem 8
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

def string_intlist_cleaner(dict):
    unwanted_keys = [k for k,v in dict.items() if type(k) != str or type(v) != list]
    for k in unwanted_keys:
        del dict[k]
    return (dict)

def int_string_cleaner(dict):
    unwanted_keys = [k for k,v in dict.items() if type(k) != int or type(v) != str]
    for k in unwanted_keys:
        del dict[k]
    return (dict)

def dict_cleaner(dict1, dict2):
    print (dict1)
    print(dict2)
    x = dict(string_intlist_cleaner(dict1))
    y = dict(int_string_cleaner(dict2))

    z = x.copy()
    z.update(y)
    print (z)
dict_cleaner(first_dict, second_dict)


# Problem 9A
filepath = '/Users/sharleenies/Desktop/Python_test/Project1-master/pokedex_basic.csv'
#
raw_pd = []
with open(filepath, 'r') as f:
    reader = csv.reader(f)



    for row in reader:
        new_row = []
        for x in list(row):
            if x.isdigit():
                new_row.append(float(x))
            elif len(x) == 0:
                new_row.append(-1)
            else:
                new_row.append(x)

        raw_pd.append(new_row)
    print (raw_pd[0:3])


# Problem 9B

filepath = '/Users/sharleenies/Desktop/Python_test/Project1-master/pokedex_basic.csv'

raw_pd = []
with open(filepath, 'r') as f:
    reader = csv.reader(f)


    raw_pd = [list(float(x) if x.isdigit() else '-1' if len(x) == 0 else x for x in row) for row in reader]

print (raw_pd[0:3])


# Problem 10

tiered_dict = {'T1.1':'V1.1',
               'T1.2':'V1.2',
               'T1.3':{'T2.1':'V2.1',
                       'T2.2':['V2.2.1','V2.2.2'],
                       'T2.3':{'T3.1':['V3.1.1','V3.1.2'],
                               'T3.2':'V3.2',
                               'T3.3':'V3.3'}},
               'T1.4':{'T2.4':{'T3.4':{'T4.1':'V4.1',
                                       'T4.2':'V4.2'},
                               'T3.5':{'T4.3':'V4.3'}},
                       'T2.5':['V2.3.1','V2.3.2']},
               }


def tiered(d, indent):
   for key, value in d.items():
      print ('\t' * indent + str(key))
      if isinstance(value, dict):
         tiered(value, indent+1)
      else:
         print ('\t' * (indent+1) + str(value))
tiered(tiered_dict,indent=0)

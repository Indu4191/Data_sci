import numpy as np



##########################
# PROBLEM 1
##########################


input_dict = {'list': [1, 2, 3, 4], 'tuple': ('cat', 'dog'), 'integer': 1, 'float': 99.99, 1: 'integer', 2: 'integer_2', 'Uppercase_string': 'ABCD', 'CHARACTER': 'C'}


def problem_1(dictionary):
    res = {}
    print dictionary
    for k, v in dictionary.items():
        if type(k) == str and k[0].islower():
            if k[0] in ('a', 'e', 'i', 'o', 'u'):
                v = 'vowel'
            else:
                v = 'consonant'

            res[k] = v

    print res
    return res

problem_1(input_dict)





##########################
# PROBLEM 2
##########################


# Write a function that operates on a dictionary and an optional list of numbers.

# Define a function that:

# - Accepts a dictionary as its first argument. The values of the dictionary should be a list of numbers.
# - Accepts an optional keyword argument that will be a list. The default should be an empty list. Name the optional keyword list `remainder`.
# - If `remainder` is empty: append a 2 to `remainder`.
# - Print the dictionary as well as `remainder`.
# - Iterate though they key: value pairs in the dictionary:
#     - For each value list of numbers, calculate the remainder of each number for each number in the `remainder` list.
#     - Create a dictionary where the keys are the numbers in the value list, and the values are the remainders of that number from the remainder list.
#     - ex: if a value in the dictionary is `[10, 9]` and `remainder` is `[2, 3]`, the new dictionary would be: `{10: [0, 1], 9: [1, 0]}`
#     - Keep the original key of the input dictionary, but change the value to the new dictionary of remainders.
# - Print out the final output dictionary.
# - Return the output dictionary.

# Notes/Hints:

# - keyword arguments are specified in functions like so: 
#     ```python
#     def example_function(arg1, kwarg1=default_value):
#     ```
# - The operator for finding the remainder of two values is "modulus": ```%```
#     ```python
#     14 % 5 == 4
#     ```
test_dict = {'A': [1, 2, 3, 4, 5], 'B': [12.1, 14.2, 20.3, 25.4], 'C': [10, 25.5, 50.9, 101]}
optional_remainder = [2, 3, 4, 5]

dictionary = test_dict
remainder = optional_remainder


def problem_2(dictionary, remainder=[]):
    res = {}

    if remainder == []:
        remainder.append(2)

    print dictionary
    print remainder

    for k, v in dictionary.items():
        r_aux = {}
        for l in v:
            rl = list()
            for r in remainder:
                rl.append(l % r)
            r_aux[l] = rl

        res[k] = r_aux

    print res
    return res

problem_2(dictionary, optional_remainder)







##########################
# PROBLEM 3
##########################


# ## Review Problem 3

# ---

# Write a function that will iterate through two lists and perform an operation.

# Define a function that:

# - Accepts two arguments that are lists of numbers (either float or integer):
# - Print both of the lists.
# - Construct a `while` loop that:
#     - Prints the current iteration number, starting at 1.
#         ```python
#         Iteration: 1
#         ```
#     - Iterates through each element of both lists at the same time using a `for` loop, assigning the number from list 1 to a variable `value1` and the number from list 2 to a variable `value2`. For example, if `list1 == [1, 2]` and `list2 == [3, 4]`, there will be two iterations through the `for` loop:
#         - Iteration 1 will have ```value1 == 1``` and ```value2 == 3```
#         - Iteration 2 will have ```value2 == 2``` and ```value2 == 4```
#     - Within the `for` loop:
#         - Multiply `value1` and `value2` together and assign it to variable `multiplied`.
#         - Print `multiplied`.
#         - If `multiplied` is greater than 300, break out of the `for` loop and `while` loop.
#         - Otherwise, multiply each element of list 1 and list 2 by 2 before continuing through the `while` loop
# - Print "Function complete."

# Notes/Hints:

# - To break out of a for loop or while loop at any time, use the `break` command.
#     - ex: 
#         ```python
#         for i in my_list: 
#             if i > 10: 
#                 break
#         ```
# - The `zip()` function will join lists/tuples element by element.
#     - ex:
#         ```python
#         zip([1, 2], [3, 4]) == [(1, 3), (2, 4)]
#         ```
#     - In a `for` loop, you can assign multiple variables at a time:
#         ```python
#         for value1, value2 in zip(list1, list2):
#         ```
# - `while True` can run a loop until a `break` condition is reached. Be careful!
list1 = [1.5, 3.5, 5.5, 7.5]
list2 = [0, 4, 8, 12]


def problem_3(list1, list2):
    print list1
    print list2

    while True:
        iteration = 1
        for value1, value2 in zip(list1, list2):
            multiplied = value1 * value2
            print multiplied
            if multiplied > 300:
                break

        if (multiplied > 300):
            break
        else:
            list1 = [2 * x for x in list1]
            list2 = [2 * x for x in list2]

    print 'Function complete.'

problem_3(list1, list2)






##########################
# PROBLEM 4
##########################


# Write a function that calculates summary statistics for distributions.
# Define a function that:
# Accepts two arguments, i and numbers.
# Prints a string indicating what the current i is.
# Calculate, without using numpy, the mean of numbers.
# Calculate, without using numpy, the median of numbers.
# Print the mean and median, for example:
#   mean: 12
#   median: 9
# Notes/Hints:
# You should define your function outside of the provided for loop, and then call it with i and numbers within the for loop.
# for i in range(1, 15, 2) assigns i from 1 to 15 with a step size of 2.

numbers = (1, 2, 3, 4, 5, 6)


def problem_4(i, numbers):
    print('iteration: {:d}'.format(i))
    
    numbers_len = len(numbers) 
    avg = sum(numbers) / float(numbers_len)

    if (numbers_len % 2 != 0):
        median_idx = numbers_len // 2
        median = numbers[median_idx]
    else:
        median_idx = numbers_len / 2
        median = (numbers[median_idx] + numbers[median_idx + 1]) / float(2)
        print('ema')

    print('  mean:   {:>7.2f}'.format(avg))
    print('  median: {:>7.2f}'.format(median))
    print('')


# Provided for loop for i and numbers:
for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    
    # Call your function here using i and numbers:
    problem_4(i, numbers)




##########################
# PROBLEM 4
##########################


# Define a function that calculates the pearson correlation coefficient between two lists of numbers.
# Your function will:
# Accept two arguments (the provided lists X and Y).
# Print the length of X and Y like so:
#   Length of X: 40
#   Length of Y: 40
# Calculate the pearson correlation coefficient between the two lists and assign the value to variable pearson_r.
# Create a variable X_deviation that is each element of X minus the mean of X.
# Create a variable Y_deviation that is each element of Y minus the mean of Y.
# Create a variable sqrt_X_deviation_sq that is the square root of the sum of the square of each element of X_deviation.
# Create a variable sqrt_Y_deviation_sq that is the same thing you just did but for Y_deviation.
# Create a variable sum_XY_deviation that is the sum of each element of X and Y multiplied by each other, in order. You can use the zip() function to iterate through two lists at the same time:
#   for x_d, y_d in zip(X_deviation, Y_deviation):
# pearson_r is equal to sum_XY_deviation divided by (sqrt_X_deviation_sq * sqrt_Y_deviation_sq).
# Print pearson_r.
# Check if it is the same as numpy's correlation function. Print np.corrcoef(X, Y)[0,1]

X = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

Y = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]


def problem_5(X, Y):
    X_mean = sum(X) / float(len(X))
    X_scaled = [x - X_mean for x in X]

    Y_mean = sum(Y) / float(len(Y))
    Y_scaled = [y - Y_mean for y in Y]

    sum_XY_scaled = sum([x * y for x, y in zip(X_scaled, Y_scaled)])

    sqrt_X_scaled_sq = np.sqrt(sum([x ** 2 for x in X_scaled]))
    sqrt_Y_scaled_sq = np.sqrt(sum([y ** 2 for y in Y_scaled]))

    pearson_r = sum_XY_scaled / (sqrt_X_scaled_sq *sqrt_Y_scaled_sq)

    print('Is it the same as numpy\'s correlation function? {}'.format(pearson_r - np.corrcoef(X, Y)[0,1] < 1e-99))
    assert (pearson_r - np.corrcoef(X, Y)[0,1]) < 1e-99
    print(pearson_r)
    print(np.corrcoef(X, Y)[0,1])


problem_5(X, Y)





##########################
# PROBLEM 6
##########################


# For this problem you will be defining a function that calculates the spearman rank correlation coefficient between two lists. Spearman's rho is a measure of how related two sets of numbers are.
# Your function will:
# Accept the provided lists of numbers defined for problem 5, X and Y.
# Calculate the rank of the numbers in the X and Y lists. The rank is a number that defines what index position each number would be if the list were in order.
# For example: say list1 = [5,2,0,9,-5], then list1_rank = [3,2,1,4,0]
# Calculating the rank is not trivial. You can use the rankdata() function from scipy.stats on a list to get the ranks of the numbers.
# Assign the rank of list X to variable X_rank and list Y to variable Y_rank.
# Manually calculate the covariance between X_rank and Y_rank as XY_rank_cov:
# Calculate X_mean: the mean of X_rank using np.mean().
# Calculate Y_mean: the mean of Y_rank using np.mean().
# Calculate X_deviation: subtract X_mean from each element of X_rank.
# Calculate Y_deviation: subtract Y_mean from each element of Y_rank.
# Calculate XY_d: multiply X_deviation with Y_deviation, element by element. You can use pythons zip() function to iterate across lists at the same time:
# for xd, yd in zip(X_deviation, Y_deviation):
# Calculate sum_XY_d: the sum of the elements in XY_d with np.sum.
# Calculate XY_rank_cov: divide sum_XY_d by len(XY_d).
# Calculate the standard deviations X_rank_std and Y_rank_std of the X_rank and Y_rank lists. You can use np.std().
# Calculate the spearman rank correlation coefficient as XY_spearman: divide XY_rank_cov by (X_rank_std * Y_rank_std).
# Print XY_spearman.
# Compare your value to the scipy function for spearman: print out spearmanr(X, Y).
import scipy.stats as st

def problem_6(X, Y):
    X_rank = st.rankdata(X)
    Y_rank = st.rankdata(Y)

    X_rank_mean = sum(X_rank) / float(len(X_rank))
    X_rank_scaled = [x - X_rank_mean for x in X_rank]

    Y_rank_mean = sum(Y_rank) / float(len(Y_rank))
    Y_rank_scaled = [y - Y_rank_mean for y in Y_rank]

    XY_rank_cov = sum([x * y for x, y in zip(X_rank_scaled, Y_rank_scaled)])

    X_rank_std = np.sqrt(sum([x ** 2 for x in X_rank_scaled]))
    Y_rank_std = np.sqrt(sum([y ** 2 for y in Y_rank_scaled]))

    XY_rho = XY_rank_cov / float(X_rank_std * Y_rank_std)

    print('Is it the same as the scipy.stats\' spearman rank correlation coefficient function? {}'.format((XY_rho - st.spearmanr(X, Y)[0]) < 1e-99))
    print(XY_rho)
    print(st.spearmanr(X, Y)[0])





##########################
# PROBLEM 7
##########################


# Write a function to calculate the root mean squared error, often written as RMSE. The RMSE is a popular measure of performance of predictions when you have a set of observed values and a set of predicted values. Your predicted values in this case are your "predictions" of what the true, observed values are.
# Your function will:
# Accept two predefined lists as arguments: true_values and predictions.
# Calculate the error between predictions and true_values as variable errors:
# Element by element, calculate the prediction minus the true value.
# Calculate the square of each element in errors and assign this to variable sq_errors.
# Calculate avg_sq_error, the mean of sq_errors.
# Calculate rmse, the square root of avg_sq_error using np.sqrt().
# Print rmse.
# Return rmse.
predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]
true_values=[-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

from sklearn.metrics import mean_squared_error


def problem_7(true_values, predictions):
    errors = [t - p for t, p in zip(true_values, predictions)]
    sq_errors = [e ** 2 for e in errors]
    avg_sq_error = sum(sq_errors) / float(len(sq_errors))
    rmse = np.sqrt(avg_sq_error)

    rmse_sklearn = np.sqrt(mean_squared_error(true_values, predictions))
    
    print('Is it the same as the sklearn metrics\' mean squared error function? {}'.format((rmse - rmse_sklearn) < 1e-99))
    print(rmse)
    print(rmse_sklearn)

    return(rmse)





##########################
# PROBLEM 8
##########################


# Define three functions to "clean up" two dictionaries and merge them together.
# Your first function, called string_intlist_cleaner should:
# Accept one argument which will be a dictionary.
# Iterate through the key:value pairs in the dictionary:
# If the key is not a string, remove the key:value pair from the dictionary.
# If the value is not a list, remove the key:value pair from the dictionary.
# Return the "cleaned" dictionary.
# Your second function, called int_string_cleaner should:
# Accept one argument which will be a dictionary.
# Iterate through the key:value pairs in the dictionary:
# If the key is not an integer, remove the key:value pair from the dictionary.
# If the value is not a string, remove the key:value pair from the dictionary.
# Return the "cleaned" dictionary.
# Your third function, called dict_cleaner should:
# Accept two arguments which will be dictionaries.
# Print the first dictionary.
# Print the second dictionary.
# Clean the first dictionary with string_intlist_cleaner() and assign to a variable.
# Clean the second dictionary with int_string_cleaner() and assign to a variable
# Combine the two cleaned dictionaries.
# Print the combined and cleaned dictionary.
# Return the combined and cleaned dictionary.
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

dict_in = first_dict
dict_in = second_dict
dict_1 = first_dict
dict_2 = second_dict


def string_intlist_cleaner(dict_in):
    keys = [k for k, v in dict_in.items() if type(k) != str or type(v) != list]
    for k in keys:
        del dict_in[k]

    return dict_in


def int_string_cleaner(dict_in):
    keys = [k for k,v in dict_in.items() if type(k) != int or type(v) != str]
    for k in keys:
        del dict_in[k]

    return dict_in


def dict_cleaner(dict_1, dict_2):
    print(dict_1)
    print(dict_2)

    dict_1 = string_intlist_cleaner(dict_1)
    dict_2 = int_string_cleaner(dict_2)

    dict_1.update(dict_2)

    print(dict_1)

    return dict_1


print(dict_cleaner(first_dict, second_dict))





##########################
# PROBLEM 9a
##########################


# Load and parse stats on Pokemon (the pokedex) from a comma separated value (.csv) file into a list of lists.
# The provided code below loads information from a comma separated value (csv) file. You need to parse this string into a more useable format. The format of the string is:
# Rows are separated by newline characters: \n
# Columns are separated by commas: ,
# All cells in the csv are double quoted. Ex: "PokedexNumber" is the first cell of the first row.
# Using for loops, create a list of lists where each list within the overall list is a row of the csv, and each element in that list is a cell in that row. Additional criteria:
# Remove the quotes from each cell item.
# Numeric column values should be converted to floats.
# There are some cells that are empty and have no information. For these cells put a -1 value in place.
# The first three lists in your pokedex list should look like:
# ['PokedexNumber', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'SpecialAttack', 'SpecialDefense', 'Speed']
# [1.0, 'Bulbasaur', 'GrassPoison', 318.0, 45.0, 49.0, 49.0, 65.0, 65.0, 45.0]
# [2.0, 'Ivysaur', 'GrassPoison', 405.0, 60.0, 62.0, 63.0, 80.0, 80.0, 60.0]


# Change this filepath to point to the location of the .csv on your own computer:
# filepath = '/Users/kiefer/github-repos/DSI-SF-4/datasets/pokemon/pokedex_basic.csv'
filepath = 'pokedex_basic.csv'

# Code to read in pokedex info
raw_pd = ''
with open(filepath, 'r') as f:
    raw_pd = f.read()


def problem_9a(raw_pd):
    df = raw_pd.replace('"', '')
    df = df.split('\n')
    df = [s.split(',') for s in df]

    for idx1 in range(len(df)):
        for idx2 in range(len(df[idx1])):
            try:
                df[idx1][idx2] = float(df[idx1][idx2])
            except ValueError:
                dummy = 'dummy'

            if df[idx1][idx2] == '':
                df[idx1][idx2] = -1

    return df


list_of_lists = problem_9a(raw_pd)

print('\n'.join([str(l) for l in list_of_lists[:3]]))






##########################
# PROBLEM 9b
##########################


# Perform the same parsing that you did with `for` loops in problem 9A, but **using only a nested list comprehensions**. A single list comprehension (with nested list comprehensions inside of it) should do all of the parsing of `raw_pd`, outputting the list of lists. Do not write any functions to call within the list comprehension.

# The output should be exactly the same as in 9A.


def problem_9b(raw_pd):
    return [[float(v) if v.isdigit() else v if v != '' else -1 for v in l.split(',')] for l in raw_pd.replace('"', '').split('\n')]


assert problem_9a(raw_pd) == problem_9b(raw_pd)




##########################
# PROBLEM 10
##########################


# Write a function that takes a tiered dictionary of dictionaries with arbitrary depth. Your function will iterate through the dictionary, printing out the contents.
# Define a function that:
# Accepts at least one argument, the predefined dictionary.
# For each key:value pair, print out the key and the value.
# If the value is also a dictionary, do the same for that dictionary, but printing out the key:value pair with tabs equivalent to the current "depth" indicating what level we are on.
# Note: tab in strings is written as \t
# Example:
# 'key1' : 'value1'
# 'key2' :
#     'key3' : 'value3'
#     'key4' : 'value4'
#     'key5' :
#         'key6': 'value6'
# 'key7' : 'value7'
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


def problem_10(dict_in, level=0):
    for k, v in dict_in.items():
        if type(v) == dict:
            print('{}\'{}\' :'.format('\t' * level, k))
            problem_10(v, level + 1)
        else:
            print('{}\'{}\' : \'{}\''.format('\t' * level, k, v))


print(problem_10(tiered_dict))





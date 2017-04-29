# Review Problem 4
'''
Write a function that calculates summary statistics for distributions.

Define a function that:

    Accepts two arguments, i and numbers.
    Prints a string indicating what the current i is.
    Calculate, without using numpy, the mean of numbers.
    Calculate, without using numpy, the median of numbers.
    Print the mean and median, for example:

    mean: 12
    median: 9

Notes/Hints:

    You should define your function outside of the provided for loop, and then call it with i and numbers within the for loop.
    for i in range(1, 15, 2) assigns i from 1 to 15 with a step size of 2.
'''
print("Problem 4")

# define a function that calculates the mean and median of the list of numbers
def summary_stats(i, numbers):
    print("i is", i, end="")

    ### calculate mean
    sum = 0
    for num in numbers:
        sum += num
    mean = sum/len(numbers)
    print(" mean =", mean, end="")

    ### calculate median
    numbers = sorted(numbers)
    # define convenient lambda functions to do the median calculations
    middle_index = lambda n: int(n/2. - 0.5)
    lower_index = lambda n: n/2 - 1
    upper_index = lambda n: n/2
    # populate the medians list:
    n = len(numbers)
    if n % 2 == 0:
        # average 2 middle values
        median = (numbers[lower_index(n)] + numbers[upper_index(n)]) / 2.
    else:
        # take middle value
        median = numbers[middle_index(n)]
    print(" median =", median)
        
# Provided for loop for i and numbers:
for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]

    # Call your function here using i and numbers:
    summary_stats(i, numbers)

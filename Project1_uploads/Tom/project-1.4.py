# Tom Croshaw - Project 1
# Problem 4 - RUN IN PYTHON 2
# Write a function that calculates summary statistics for distributions.

import numpy as np

def mean_median(i, numbers):
    print ("i: ",str(i)) # Prints a string indicating what the current i is
    mean = float(sum(numbers)/len(numbers)) #calculate mean of numbers
    def median(lst): # Sub-function to calculate the median of numbers (depends on the length of the list)
        num_sort = sorted(numbers)
        if len(num_sort) < 1:
            return None
        elif len(num_sort) %2 == 1:
            return num_sort[((len(num_sort)+1)/2)-1]
        else:
            return float(sum(num_sort[(len(num_sort)/2)-1:(len(numbers)/2)+1]))/2.0
    median = median(numbers) #call median function
    print "Mean: ", mean
    print "Median: ", median

# Check output with provided for-loop
for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    print mean_median(i, numbers)

# Review Problem 2
'''
Write a function that operates on a dictionary and an optional list of numbers.

Define a function that:

    Accepts a dictionary as its first argument. The values of the dictionary should be a list of numbers.
    Accepts an optional keyword argument that will be a list. The default should be an empty list. Name the optional keyword list remainder.
    If remainder is empty: append a 2 to remainder.
    Print the dictionary as well as remainder.
    Iterate though they key:value pairs in the dictionary:
        For each value list of numbers, calculate the remainder of each number for each number in the remainder list.
        Create a dictionary where the keys are the numbers in the value list, and the values are the remainders of that number from the remainder list.
        ex: if a value in the dictionary is [10,9] and remainder is [2,3], the new dictionary would be: {10:[0, 1], 9:[1, 0]}
        Keep the original key of the input dictionary, but change the value to the new dictionary of remainders.
    Print out the final output dictionary.
    Return the output dictionary.

Notes/Hints:

    keyword arguments are specified in functions like so:

    def example_function(arg1, kwarg1=default_value):
'''
print("Problem 2")

# print out key/value pairs from dictionary
def print_dict(input_dict):
    for key, values in input_dict.items():
        print(key, ':', values)
        
# define a function that loops through the dictionary entries and processes as per requirements
def process_dict(input_dict, remainder=[]):
    # if remainder is empty append a 2
    if not remainder:
        remainder.append(2)

    print("\nInput dictionary:")
    print_dict(input_dict)
    print("Remainder:", remainder)
	
    output_dict = {}
    for keys,values in input_dict.items():
        for val in values:
            rem_list = []
            # calculate the remainder of each number for each number in the remainder list
            for rem in remainder:
                #print(val % rem)
                rem_list.append(int(val % rem))
            #print(val, rem_list)
            # keys are the numbers in the value list, values are the remainders of that number from the remainder list
            output_dict[val] = rem_list

    print("\nOutput dictionary:")
    print_dict(output_dict)
    return output_dict

test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]
process_dict(test_dict, optional_remainder)

#input_dict = {'list1':[1,2,3,4], 'list2':[100,200,300], 'list3':[1000,2000,3000,4000,5000]}
#remainder = [3,4]
#process_dict(input_dict, remainder)
# try with another dictionary and list
#test_dict = {'list1':[10,9]}
#optional_remainder = [2,3]
#process_dict(test_dict, optional_remainder)

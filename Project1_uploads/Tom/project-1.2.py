# Tom Croshaw - Project 1
# Problem 2 - PYTHON 3
# Write a function that operates on a dictionary and an optional list of numbers.

test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

def dict_create(dictInput,remainder=[]):
    if remainder == None:
        remainder = 2
    print ('Input Dictionary: ',dictInput)
    print ('Remainder: ', remainder)
    # Create remainder
    rm = [[float(a % b) for a, b in zip(dictInput[key], remainder)] for key in dictInput]
    print (rm) # print remainder output as a check
    new_keys = [dictInput[key] for key in dictInput]
    print (new_keys)
    # print new keys as a check
    pair_lists = zip(new_keys, rm) #pair new keys
    # Create empty dictionary and iterate through the key:value pairs, adding into the new dictionary
    dict_int = {}
    for new_keys, rm in pair_lists:
        for key in new_keys:
            dict_int[key] = rm
    print ('Output Dictionary: ',dict_int)

print (dict_create(test_dict,optional_remainder))

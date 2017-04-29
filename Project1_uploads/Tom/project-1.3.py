# Tom Croshaw - Project 1
# Problem 3 - PYTHON 3
# Write a function that will iterate through two lists and perform an operation.

def operation(list1,list2):
    print ('List 1: ',list1) # print first input list
    print ('List 2: ',list2) # print second input list
    i = 0
    while True: # create a while loop
        i += 1
        print (("Iteration: "), i)
        for value1, value2 in zip(list1, list2): # Iterates through each element of both lists at the same time using a for loop, assigning the number from list 1 to a variable value1 and the number from list 2 to a variable value2.
            multiplied = value1 * value2 # Multiply value1 and value2 together and assign it to variable multiplied.
            print (multiplied) # Print multiplied.
        if multiplied > 300: # If multiplied is greater than 300, break out of the for loop and while loop.
            break
        else: # Otherwise, multiply each element of list 1 and list 2 by 2 before continuing through the while loop
            list1 = [i * 2 for i in list1]
            list2 = [i * 2 for i in list2]

    print ('function complete')


# Test function with two provided loops
list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]

print (operation(list1,list2))

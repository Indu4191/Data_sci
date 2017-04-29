# Review Problem 3
'''
Write a function that will iterate through two lists and perform an operation.

Define a function that:

    Accepts two arguments that are lists of numbers (either float or integer):
    Print both of the lists.
    Construct a while loop that:
        Prints the current iteration number, starting at 1.

        Iteration: 1

        Iterates through each element of both lists at the same time using a for loop, assigning the number
        from list 1 to a variable value1 and the number from list 2 to a variable value2.
        For example, if list1 == [1, 2] and list2 == [3, 4], there will be two iterations through the for loop:
            Iteration 1 will have value1 == 1 and value2 == 3
            Iteration 2 will have value2 == 2 and value2 == 4
        Within the for loop:
            Multiply value1 and value2 together and assign it to variable multiplied.
            Print multiplied.
            If multiplied is greater than 300, break out of the for loop and while loop.
            Otherwise, multiply each element of list 1 and list 2 by 2 before continuing through the while loop
    Print "Function complete."

Notes/Hints:

    To break out of a for loop or while loop at any time, use the break command.
        ex:

        for i in my_list: 
              if i > 10: 
                  break

    The zip() function will join lists/tuples element by element.
        ex:

        zip([1,2], [3,4]) == [(1, 3), (2, 4)]

        In a for loop, you can assign multiple variables at a time:

        for value1, value2 in zip(list1, list2):

    while True can run a loop until a break condition is reached. Be careful!
'''
print("Problem 3")

# define a function that loops through the lists and processes as per requirements
def process_lists(numlist1, numlist2):
    print("first list =", numlist1, "second list =", numlist2)
    iteration = 1
    multiplied = 0
    
    while iteration < 1000: # set a high limit just in case to prevent infinite looping
        print("iteration ", iteration)
        iteration += 1
        
        # use zip for easier looping of both lists
        for value1, value2 in zip(numlist1, numlist2):
            #print(value1, value2, " ", end="")
            multiplied = value1 * value2
            print("multiplied = ", multiplied)
            
            # break out of for loop if termination condition reached
            if multiplied > 300:
                break

        # break out of while loop if termination condition reached
        # see function process_lists_2 below for alternative solution to 2 breaks
        if multiplied > 300:
            print("Function complete.")
            break

        # update each element in both lists by 2
        numlist1 = [i*2 for i in numlist1]
        numlist2 = [i*2 for i in numlist2]
    
list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]
process_lists(list1, list2)

#process_lists([1,2,3,4,5], [1.1, 2.2, 3.3, 4.4, 5.5])
#process_lists([1,2,3,4,5], [1.1, 2.2, 3.3, 4.4, 5.5])
#process_lists([1.0,2.0,3.0,4.0,5.0], [1.1, 2.2, 3.3, 4.4, 5.5])

def process_lists_2(numlist1, numlist2):
    print("first list =", numlist1, "second list =", numlist2)
    iteration = 1
    multiplied = 0
    
    class BreakOut(Exception): pass
    try:
        while iteration < 1000: # set a high limit just in case to prevent infinite looping
            print("iteration ", iteration)
            iteration += 1
            
            # use zip for easier looping of both lists
            for value1, value2 in zip(numlist1, numlist2):
                #print(value1, value2, " ", end="")
                multiplied = value1 * value2
                print("multiplied = ", multiplied)
                
                # break out of for and while loop if termination condition reached
                if multiplied > 300:
                    raise BreakOut

            # update each element in both lists by 2
            numlist1 = [i*2 for i in numlist1]
            numlist2 = [i*2 for i in numlist2]

    except BreakOut:
        print("Function complete.")
        pass
    

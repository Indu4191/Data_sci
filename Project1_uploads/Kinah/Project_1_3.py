#Problem 3
list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]


def function(list1, list2):
    #print(list1)
    #print(list2)
    i = 1
    while len(list1) == 4: 
        for value1, value2 in zip(list1, list2):
            print('Iteration:' + str(i))
            i += 1
            multiplied = value1 * value2
            print(multiplied)
        if multiplied < 300:
            list1 = [x * 2 for x in list1]
            list2 = [y * 2 for y in list2]
        else:
            print('Function complete')
            break
    
function(list1, list2)
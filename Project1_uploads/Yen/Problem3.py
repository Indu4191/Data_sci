


list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]

def Problem3(list1,list2):
    print(list1)
    print(list2)
    #print the iteration number
    counter = 1
    multiplied = 0
    while counter < 5:
        print('Iteration: '+str(counter))

    #iterate through list1 and list2, assigning each item to value1 and value2#
        list3 = list1
        list4 = list2
        for value1, value2 in zip(list1,list2):
            #assign multiplied to product of value1 and value2
            multiplied = value1 * value2
            print('multiplied: '+ str(multiplied))
            counter +=1
            #break loop if multiplied > 300
            if multiplied > 300:
                break
            else:
                list3 = []
                list4 = []
                for x in list1:
                    x = x * 2
                    list3.append(x)
                for y in list2:
                    y = y * 2
                    list4.append(y)
        for value1, value2 in zip(list3,list4):
            #assign multiplied to product of value1 and value2
            multiplied = value1 * value2
            print('multiplied: '+ str(multiplied))
            counter += 1
            #break loop if multiplied > 300
            if multiplied > 300:
                break
    print(list1)
    print(list2)
    print(list3)
    print(list4)

print('Function Complete')

Problem3(list1,list2)

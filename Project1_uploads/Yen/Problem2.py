


test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

def Problem2(test_dict,list_remainder):
    if len(list_remainder) == 0:
        list_remainder.append(2)
    print(test_dict)
    print(list_remainder)

    final_dict = {}

    for key, value in test_dict.items():
        #run through each key
        answer_dict = {}
        for v in value:
            #calculate remainder of v in value
            #v is key, remainder is value
            remainder = [float(round(v % r)) for r in list_remainder]
            answer_dict[v] = remainder
            final_dict[key] = answer_dict
    print(final_dict)


Problem2(test_dict, optional_remainder)

#Problem 2
test_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
optional_remainder = [2,3,4,5]

def function(test_dict, optional_remainder):
    if len(optional_remainder) == 0:
     optional_remainder.append(2)
    new_dict1 = {}
    for k,v in test_dict.items():
        new_dict = {}
        for x in v:
            remainder_list = [(x % a) for a in optional_remainder]
            new_dict[x] = remainder_list
        new_dict1[k] = new_dict 

    print(new_dict1)
        
    # print(test_dict)
    # print(optional_remainder)
function(test_dict, optional_remainder)
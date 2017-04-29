#Problem 8
first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}

def string_intlist_cleaner(first_dict):
    a = []
    for k, v in first_dict.items():
        if type(k) != str or type(v) != list:
            a.append(k)
    for k in a:
        del first_dict[k]

    #print(first_dict)

string_intlist_cleaner(first_dict)
def int_string_cleaner(second_dict):
    b = []
    for k, v in second_dict.items():
        if type(k) != int or type(v) != str:
            b.append(k)
    for k in b:
        del second_dict[k]
        
    #print(second_dict)

int_string_cleaner(second_dict)

def dict_cleaner(first_dict, second_dict):
    #print(first_dict)
    #print(second_dict)
    a = first_dict
    b = second_dict
    combined_dict = a.update(b)
    print(combined_dict) #Return none value
    print(a) #Return the cleaned dictionary

dict_cleaner(first_dict, second_dict)
import string

first_dict = {'A':(1,2), 'B':[1,2,3,4,4], 'C':[0,9], 1:(1,1,1), 12:None, 'D':None, 'E':12.777}
second_dict = {'1':('a','b'), 2:{1:23.3}, 3:'four', 4:'five', 'five':['six', 'seven'], 8:'nine'}#

def string_intlist_cleaner(dict1):
   cleaned_1 = dict1
   for k in list(cleaned_1.keys()):
       if type(k) != str:
           del cleaned_1[k]
   for k,v in list(cleaned_1.items()):
       if type(v) != list:
           del cleaned_1[k]
   return cleaned_1

def int_string_cleaner(dict2):
   cleaned_2 = dict2
   for k in list(cleaned_2.keys()):
       if type(k) != int:
           del cleaned_2[k]
   for k,v in list(cleaned_2.items()):
       if type(v) != str:
           del cleaned_2[k]
   return cleaned_2

def dict_cleaner(dict1,dict2):
   print('First dict: ' + str(dict1))
   print('Second dict: ' + str(dict2))
   really_clean1 = string_intlist_cleaner(dict1)
   really_clean2 = int_string_cleaner(dict2)
   combined_dict = {**really_clean1, **really_clean2}
   print('Combined and cleaned dict: ' + str(combined_dict))
   print('Cleaned dict1: ' + str(really_clean1))
   print('Cleaned dict2: ' + str(really_clean2))
   return really_clean1
   return really_clean2
   return combined_dict

dict_cleaner(first_dict, second_dict)

import json

tiered_dict = {'T1.1':'V1.1',
               'T1.2':'V1.2',
               'T1.3':{'T2.1':'V2.1',
                       'T2.2':['V2.2.1','V2.2.2'],
                       'T2.3':{'T3.1':['V3.1.1','V3.1.2'],
                               'T3.2':'V3.2',
                               'T3.3':'V3.3'}},
               'T1.4':{'T2.4':{'T3.4':{'T4.1':'V4.1',
                                       'T4.2':'V4.2'},
                               'T3.5':{'T4.3':'V4.3'}},
                       'T2.5':['V2.3.1','V2.3.2']},
               }

def Problem10(dict):
    print(json.dumps(dict, sort_keys=True, indent = 4))



Problem10(tiered_dict)

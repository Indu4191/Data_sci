###################################################################
#PROBLEM 9b
###################################################################

# Change this filepath to point to the location of the .csv on your own computer:
filepath = '/home/srikanta/DS/Project1/pokedex_basic.csv'

# Code to read in pokedex info
raw_pd = ''
lst_final=[]
with open(filepath, 'r') as f:
    raw_pd = f.read()
    raw_pd = raw_pd.replace('"','')
    lst_final = [[float(w) if w.isdigit() else - 1 if w =='' else w 
                 for w in l.split(",")] for l in raw_pd.splitlines()]
    print (lst_final)
f.close()
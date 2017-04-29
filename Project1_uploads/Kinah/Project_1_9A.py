#Problem 9A
import csv
# Change this filepath to point to the location of the .csv on your own computer:
filepath = ('/Users/User/Desktop/Data Science Immersive/Projects/pokedex_basic.csv')

# Code to read in pokedex info
raw_pd = ''
updated = []
with open(filepath, 'r') as f:
    raw_pd = f.read()

    for row in raw_pd.splitlines():
        new_data = row.split(",")
        new_list = []
        for x in new_data:
            y = x.replace('"','')
            if y.isdigit():
                new_list.append(float(y)) #convert values to float
            elif y == '':
                new_list.append(-1)
            else:
                new_list.append(y)
        updated.append(new_list)

print(updated[0:3])
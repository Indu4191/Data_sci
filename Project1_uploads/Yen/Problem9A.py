import csv

# Change this filepath to point to the location of the .csv on your own computer:
filepath = '/Users/lohyenwei/Desktop/data_science/Project1/Project1/pokedex_basic.csv'

# Code to read in pokedex info
raw_pd = []
with open(filepath, 'r') as f:
    raw_pd = csv.reader(f)

    pokedex = []
    for row in raw_pd:
        for x in row:
            if x.isdigit() == True:
                pokedex.append(float(x))
            elif len(x) == 0:
                x = -1
                pokedex.append(x)
            else:
                pokedex.append(x)

pokelist = [pokedex[x:x + 9]for x in range(0, len(pokedex),9)]

print(pokelist[0])
print(pokelist[1])
print(pokelist[2])

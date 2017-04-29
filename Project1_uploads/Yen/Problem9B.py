import csv

filepath = '/Users/lohyenwei/Desktop/data_science/Project1/Project1/pokedex_basic.csv'

# Code to read in pokedex info
raw_pd = []
with open(filepath, 'r') as f:
    raw_pd = csv.reader(f)

    pokedex = [list(float(x) if x.isdigit() else "-1" if len(x) == 0 else x for x in row)for row in raw_pd]
print(pokedex[0])
print(pokedex[1])
print(pokedex[2])

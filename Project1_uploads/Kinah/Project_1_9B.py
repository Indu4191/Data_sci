#Problem 9B
import csv
# Change this filepath to point to the location of the .csv on your own computer:
filepath = ('/Users/User/Desktop/Data Science Immersive/Projects/pokedex_basic.csv')

# Code to read in pokedex info
raw_pd = ''
updated = []
with open(filepath, 'r') as f:
    raw_pd = f.read()
    raw_pd = raw_pd.replace('"','')
    updated = [[float(y) if y.isdigit() else - 1 if y =='' else y 
                 for y in row.split(",")] for row in raw_pd.splitlines()]

print(updated[0:3])
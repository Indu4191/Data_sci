# Review Problem 9A
'''
Load and parse stats on Pokemon (the pokedex) from a comma separated value (.csv) file into a list of lists.

The provided code below loads information from a comma separated value (csv) file. You need to parse this string into a more useable format. The format of the string is:

    Rows are separated by newline characters: \n
    Columns are separated by commas: ,
    All cells in the csv are double quoted. Ex: "PokedexNumber" is the first cell of the first row.

Using for loops, create a list of lists where each list within the overall list is a row of the csv, and each element in that list is a cell in that row. Additional criteria:

    Remove the quotes from each cell item.
    Numeric column values should be converted to floats.
    There are some cells that are empty and have no information. For these cells put a -1 value in place.

The first three lists in your pokedex list should look like:

['PokedexNumber', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'SpecialAttack', 'SpecialDefense', 'Speed']
[1.0, 'Bulbasaur', 'GrassPoison', 318.0, 45.0, 49.0, 49.0, 65.0, 65.0, 45.0]
[2.0, 'Ivysaur', 'GrassPoison', 405.0, 60.0, 62.0, 63.0, 80.0, 80.0, 60.0]
'''
print("Problem 9a")

filepath = './pokedex_basic.csv'

# Code to read in pokedex info

data = ''
with open(filepath, 'r') as f:
    data = f.read()

# split on carriage returns to get each row
data = data.split('\n')
# create empty list for rows
row_data = []

# loop through each row
for row in data:
    # split on commas to get each column
    columns = row.split(',')
    # remove the quotes from each cell item
    columns = [col.strip('"') for col in columns]
    
    # create empty list for columns
    col_data = []
    # loop through each column
    for col in columns:
        # convert to float where necessary, change to -1 if empty value
        if col.isdigit():
            col_data.append(float(col))
        elif col == '':
            col_data.append(-1)
        else:
            col_data.append(col)

    row_data.append(col_data)

print(row_data[0])
print(row_data[1])
print(row_data[2])

# Review Problem 9B
'''
Perform the same parsing that you did with for loops in problem 9A, but using only a nested list comprehensions. A single list comprehension (with nested list comprehensions inside of it) should do all of the parsing of raw_pd, outputting the list of lists. Do not write any functions to call within the list comprehension.

The output should be exactly the same as in 9A.
'''
print("\nProblem 9b")

import string

alphabet = list(string.ascii_lowercase)
vowels = list('aeiou')
characters = ['a','f',None,'k','l','1',12,'e','e',-1,'i','b','p']
converted = ['v' if x in vowels else 'c' if (x in alphabet and x not in vowels) else '?' for x in characters]

# Code to read in pokedex info
data = ''
with open(filepath, 'r') as f:
    data = f.read()

#build up statement bit by bit
#row_data = [row.split(',') for row in data.split('\n')]
#row_data = [[col.strip('"') for col in row.split(',')] for row in data.split('\n')]

# split on carriage returns to get each row, split on commas to get each column,
# remove the quotes from each cell item, convert to float where necessary, change to -1 if empty value
row_data = [[float(x) if x.isdigit() else -1 if x == '' else x for x in [col.strip('"') for col in row.split(',')]] for row in data.split('\n')]

print(row_data[0])
print(row_data[1])
print(row_data[2])

# Tom Croshaw - Project 1
# Problem 9B - PYTHON 3
# Perform the same parsing that you did with for loops in problem 9A, but using only a nested list comprehensions.

raw_pd = ''
with open('pokedex_basic.csv', 'r') as f:
    raw_pd = f.read()
    raw_data = raw_pd.replace('"', '').splitlines()
    # Nested list comprehension version of 9A: first action: if cell is empty append '-1'
    output_list = [[-1 if cell == None\
     # Checks whether the string consists of digits only and appends the float version of the cell
     else float(cell) if cell.isdigit() == True\
     # If not, append the original (string) cell to the new_line list
     else cell\
     # Iterate through the split cells in each line
     for cell in line.split(',')]\
     # Iterate through the lines in the data
     for line in raw_data]
# Print out the first 3 lists
print ('Top 3 rows:',output_list[:3])

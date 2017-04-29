# Tom Croshaw - Project 1
# Problem 9A - PYTHON 3
# Change this filepath to point to the location of the .csv on your own computer:
# filepath = '/Users/kiefer/github-repos/DSI-SF-4/datasets/pokemon/pokedex_basic.csv'

# Code to read in pokedex info
# Using for loops, create a list of lists where each list within the overall list is a row of the csv, and each element in that list is a cell in that row. Additional criteria:

raw_pd = ''
with open('pokedex_basic.csv', 'r') as f:
    raw_pd = f.read()
    raw_data = raw_pd.replace('"', '').splitlines() #Remove quotations and split lines
    output_list = []
    for line in raw_data: # Iterate through the lists in each data
        line = line.split(',') # Split the cells by commas
        new_line = [] # Create a new list for each line of data
        for cell in line:
            # If cell is empty append '-1'
            if cell == None:
                new_line.append(-1)
            # Checks whether the string consists of digits only and appends the float version of the cell
            if cell.isdigit() == True:
                new_line.append(float(cell))
            # If not, append the original (string) cell to the new_line list
            else:
                new_line.append(cell)
        output_list.append(new_line) # Appending new lines (lists) to the 'output_list' list variable
    # Check the full list is created
    for list in output_list:
        print (list)
# Print out the first 3 lists
print ('Top 3 rows:',output_list[:3])

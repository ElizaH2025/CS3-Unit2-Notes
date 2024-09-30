# importing libraries "as" aliases
import numpy as np
import pandas as pd

# *** Pandas' SERIES Object ***
# Series are 1D arrays of indexed data

# Created Series from a list/array
data = pd.Series([0.25, 0.5, 0.75, 1.0])

print(data.values) # looks like a list
print(data.index) # range computed for indices

print()

# Access Series data by index
print("Getting one value from Series:", data[1])

print()

print("Getting multiple values will also shows indices:")
print(data[0:3]) # not including stop index

print()

# Series are like arrays but with EXPLICIT indexing
grades = pd.Series([9, 10, 11, 12], index = ['Freshman:', 'Sophmore:', 'Junior:', 'Senior:'])
print('Seniors are in grade:',grades['Senior:'])

print()

# Can also create a Series from a dictionary
cookies_dict = {'Double Chocolate:': 5,
                'Chocolate Chip:': 8.5,
                'Oatmeal Raisin:': 9,
                'Snickerdoodle:': 10,
                'DIRT:': -1 }
cookies = pd.Series(cookies_dict)
print(cookies)

# Access utem by index
print('Rating od dirt cookies: ', cookies['DIRT:'])
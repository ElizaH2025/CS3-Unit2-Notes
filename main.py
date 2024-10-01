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

print()
# Access utem by index
print('Rating of dirt cookies: ', cookies['DIRT:'])
print()

# DataFrame is like a 2D array or specialized dictionary
cookies_df = pd.DataFrame(cookies, columns=['Ratings'])
print(cookies_df)

# Add a column to our DataFrame
cookies_df['Allergens'] = ['True','True', 'True', 'True', 'False']
print(cookies_df)

print()

# Another way to add a column
cookies_df['sweetness'] = {'Double Chocolate:': 10,
                'Chocolate Chip:': 8.5,
                'Oatmeal Raisin:': 7,
                'Snickerdoodle:': 8,
                'DIRT:': -1 }

print(cookies_df)

print()

print('****** DATA SELECTION ******')
data = pd. Series(['E','l','i','z', 'a'], index=[5, 12, 8, 26, 1])

# Indexing uses the explicit index
print(data[5])

#Slicing (getting multiples values) uses IMPLICIT index
print(data[2:4]) #not getting expected output

# Instead, use the LOC attribute to get a slice that uses explicit indices
print(data.loc[5:1]) #includes items at index 5

# Not as common, iLoc uses implicit indices
print(data,iloc[5:1]) # doesn't include second item
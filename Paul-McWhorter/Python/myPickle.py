# Python Tutorial 14: Saving and Reading Data Files With Pickle (Paul McWhorter)

import pickle

fruits = ['apples', 'oranges', 'bananas']

x = 7
y = 3.14

nuts = ['pecans', 'almonds']

grades = [99, 100, 56, 77, 85]

dataSet = [fruits, x, y, nuts, grades]

# Write data as a binary file
with open('myData.pkl', 'wb') as f:

    pickle.dump(dataSet, f)

# Read binary file
with open('myData.pkl', 'rb') as f2:
    p0 = pickle.load(f2)

for dt in p0:
  print(dt)

# Use python template literal to concatenate p variables w/ i and print variables 
# containing pickle data
# for i in range(1):
#     print(eval("p" + str(i)))

#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# opens data file and reads it
data = [] # allows a space for data to populate

with open('RNG_output.txt') as fp:
    for line in fp:
        line = line[:-2]
        line=float(line)
        data.append(line)

# converts data into an array for easier histogram creation
data = np.asarray(data)

# create histogram of our data
n, bins, patches = plt.hist(data[data<=1], 100, density=True, facecolor='orange', alpha=0.75)

# plot formating options
plt.xlabel('Randomly Generated Number')
plt.ylabel('Probability')
plt.title('Frequency of Randomly Generated Numbers')
plt.grid(True)

# show figure (program only ends once closed
plt.show()


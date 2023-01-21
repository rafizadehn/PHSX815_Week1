#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# opens data file and reads it
data = []

with open('RNG_output.txt') as fp:
    for line in fp:
        line = line[:-2]
        line=float(line)
        data.append(line)

data = np.asarray(data)

# create histogram of our data
n, bins, patches = plt.hist(data[data<=1], 50, density=True, facecolor='g', alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)

# show figure (program only ends once closed
plt.show()


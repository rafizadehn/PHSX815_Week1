#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
datafile = 'RNG_output.txt'
myx = np.loadtxt(datafile, delimiter=',', dtype=str)
    # create histogram of our data
n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

print(myx)    

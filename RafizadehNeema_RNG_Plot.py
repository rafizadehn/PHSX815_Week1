#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

#datafile = 'RNG_output.txt'
#data = np.loadtxt(datafile, dtype=list)
#myx = list(data)
#print(data)


# opening the file in read mode
my_file = open("RNG_output.txt", "r")

# reading the file
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace('\n', ' ').split(".")

# printing the data
print(data_into_list)
my_file.close()


    # create histogram of our data
n, bins, patches = plt.hist(data_into_list, 50, density=True, facecolor='g', alpha=0.75)

    # plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)

    # show figure (program only ends once closed)
plt.show()
    

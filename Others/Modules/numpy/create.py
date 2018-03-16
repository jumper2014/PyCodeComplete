#!/usr/bin/env python
# coding=utf-8

import numpy as np

a = np.zeros((2, 2))  # Create an array of all zeros
print a  # Prints "[[ 0.  0.]
#          [ 0.  0.]]"

b = np.ones((1, 2))  # Create an array of all ones
print b  # Prints "[[ 1.  1.]]"

c = np.full((2, 2), 7)  # Create a constant array
print c  # Prints "[[ 7.  7.]
#          [ 7.  7.]]"

d = np.eye(2)  # Create a 2x2 identity matrix
print d  # Prints "[[ 1.  0.]
#          [ 0.  1.]]"

e = np.random.random((2, 2))  # Create an array filled with random values
print e  # Might print "[[ 0.91940167  0.08143941]
#               [ 0.68744134  0.87236687]]"
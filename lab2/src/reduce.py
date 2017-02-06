# !/usr/bin/env python
# Reduce function for computing matrix multiply A*B

# Input arguments:
# variable n should be set to the inner dimension of
# the matrix product (i.e., the number of columns of A/rows of B)

import sys
# import string
# import numpy

# number of columns of A/rows of B
n = int(sys.argv[1])

# Create data structures to hold the current
# row/column values (if needed; your code goes here)

arow = [0.0] * n
bcol = [0.0] * n

currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    # Remove leading and trailing whitespace
    line = line.strip()

    # Get key/value
    key, value = line.split('\t', 1)

    # Parse key/value input (your code goes here)
    keys = key.split(' ')
    row = int(keys[0])
    col = int(keys[1])
    values = value.split(' ')

    matrix = values[0]
    pos = int(values[1])
    val = float(values[2])

    # If we are still on the same key...
    if key == currentkey:
        if matrix == 'A':
            arow[pos] = val
        elif matrix == 'B':
            bcol[pos] = val

    # Otherwise, if this is a new key...
    else:
        # If this is a new key and not the first key we've seen
        if currentkey:
            currentkeys = currentkey.split(' ')

            result = 0.0
            for i in range(n):
                result += arow[i] * bcol[i]
            print 'C,{},{},{}'.format(currentkeys[0], currentkeys[1], result)

        currentkey = key
        arow = [0.0] * n
        bcol = [0.0] * n
        if matrix == 'A':
            arow[pos] = val
        elif matrix == 'B':
            bcol[pos] = val

# Compute/output result for the last key
result = 0.0
currentkeys = currentkey.split(' ')
for i in range(n):
    result += arow[i] * bcol[i]
print 'C,{},{},{}'.format(currentkeys[0], currentkeys[1], result)

# PROBLEM DESCRIPTION:
# You are given a sequence of integers a1,a2,a3.....an. You are free to replace 
# any integer with any other positive integer. How many integers must be replaced 
# to make the resulting sequence strictly increasing?

# INPUT FORMAT:
# The first line of the test case contains an integer  - the number of entries in the sequence.
# The next line contains  space separated integers where the  integer is .

# OUTPUT FORMAT:
# Output the minimal number of integers that should be replaced to make the sequence strictly increasing.


# SAMPLE INPUT - 1                             SAMPLE OUTPUT - 1
# 3                                            0
# 4 10 20

# SAMPLE INPUT - 2                             SAMPLE OUTPUT - 2 
# 6                                            1
# 1 7 10 2 20 22

# SAMPLE INPUT - 3                             SAMPLE OUTPUT - 3
# 5                                            3 
# 1 2 2 3 4 


# EXPLANATION
# In the first sample input, we need not replace anything, hence the output is 0.
# In the second sample input, we can replace 2 with any integer between 11 and 19 to make the sequence strictly increasing, hence the output is 1.
# In the third sample input, we can obtain 1, 2, 3, 4, 5 by changing the last three elements of the sequence.

#!/bin/python3

import os
import sys

#
# Complete the modifySequence function below.
#
def modifySequence(arr):
    replaceCount = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            arr[i] = arr[i-1] + 1
            replaceCount += 1

    return replaceCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

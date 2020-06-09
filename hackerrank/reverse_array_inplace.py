# PROBLEM DESCRIPTION:
# Given an array, , of  integers, print each element in reverse order as a single line of space-separated integers.

# INPUT FORMAT
# The first line contains an integer, N (the number of integers in A).
# The second line contains N  space-separated integers describing A.

# OUTPUT FORMAT
# Print all N integers in A in reverse order as a single line of space-separated integers.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# 0 3 4 2                                           2 4 3 0

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    if not a:
        return []
    
    for i in range(0, len(a)//2):
        a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
    
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

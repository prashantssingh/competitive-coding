# PROBLEM DESCRIPTION
# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks 
# with matching colors there are.

# For example, there are `n = 7` socks with colors `ar = [ 1, 2, 1, 2, 1, 3, 2 ]`. There is one pair 
# of color `1` and one of color `2`. There are three odd socks left, one of each color. The number of 
# pairs is `2`.

# FUNCTION DESCRIPTION
# Complete the sockMerchant function in the editor below. It must return an integer representing the 
# number of matching pairs of socks that are available.
# sockMerchant has the following parameter(s):
# n: the number of socks in the pile
# ar: the colors of each sock


# INPUT FORMAT
# The first line contains an integer `n`, the number of socks represented in `ar`.
# The second line contains `n` space-separated integers describing the colors `ar[i]` of the socks in the pile.

# OUTPUT FORMAT
# Return the total number of matching pairs of socks that John can sell.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# 9                                                 3
# 10 20 20 10 10 30 50 10 20
# Sample Output

# EXPLANATION
# There are two pair of color `10` and one of color `20`. There are three odd socks left, `20, 30, 50`. The number of 
# pairs is `3`.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

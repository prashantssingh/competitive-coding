#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindrome(s):
    result = set()
    def count(left, right):
        currCount = 0
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            if s[left:right+1] not in result:
                currCount += 1
                result.add(s[left:right+1])
            left -= 1
            right += 1
        return currCount

    countPalindrome = 0
    length = len(s)
    for i in range(length):
        countPalindrome += count(i,i)
        countPalindrome += count(i,i+1)

    return countPalindrome
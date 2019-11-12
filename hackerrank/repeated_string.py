# PROBLEM DESCRIPTION
# Lilah has a string, `s`, of lowercase English letters that she repeated infinitely many times.
# Given an integer, , find and print the number of letter a's in the first `n` letters of Lilah's infinite string.
# For example, if the string `s = "abcac"` and `n = 10`, the substring we consider is `abcacabcac`, the first `10` characters of her infinite string. There are `4` occurrences of a in the substring.

# FUNCTION DESCRIPTION
# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length `n` in the infinitely repeating string.
# repeatedString has the following parameter(s):
# s: a string to repeat
# n: the number of characters to consider


# INPUT FORMAT
# The first line contains a single string, `s`.
# The second line contains an integer, `n`.

# INPUT FORMAT
# Print a single integer denoting the number of letter a's in the first `n` letters of the infinite string created by repeating `s` infinitely many times.

# SAMPLE INPUT - 1                             SAMPLE OUTPUT - 1
# aba                                          7
# 10

# EXPLANATION
# The first `n = 10` letters of the infinite string are abaabaabaa. Because there are `7` a's, we print `7` on a new line.

# SAMPLE INPUT - 2                             SAMPLE OUTPUT - 2
# a                                            1000000000000
# 1000000000000

# EXPLANATION
# Because all of the first `n = 1000000000000` letters of the infinite string are a, we print n on a new line.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

def generateString(strPattern, length):
    quotient, remainder = divmod(length, len(strPattern))
    return strPattern*quotient + strPattern[:remainder]

def getCharIndices(char, targetString):
    return [i for i, letter in enumerate(targetString) if letter == char]

# Complete the repeatedString function below.
def repeatedString(s, n):
    char = 'a'
    return len(getCharIndices(char, generateString(s, n)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

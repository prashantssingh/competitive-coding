# PROBLEM DESCRIPTION
# You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
# The elements of the first array are all factors of the integer being considered
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

# For example, given the arrays `a = [2,6]` and `b = [24,36]`, there are two numbers between them: 6 and 12. `6 % 2 = 0`, 
# `6 % 6 = 0`, `24 % 6 = 0` and `36 % 6 = 0` for the first value. Similarly, `12 % 2 = 0`, `12 % 6 = 0` and `24 % 12 = 0`, `36 % 12 = 0`.

# FUNCTION DESCRIPTION
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
# getTotalX has the following parameter(s):
# a: an array of integers
# b: an array of integers

# INPUT FORMAT
# The first line contains two space-separated integers, n and m, the number of elements in array a and the number of elements in array b.
# The second line contains n distinct space-separated integers describing a[i] where `0 <= i < n`.
# The third line contains m distinct space-separated integers describing b[j] where `0 <= j < m`.

# OUTPUT FORMAT
# Print the number of integers that are considered to be between a and b.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# 2 3                                               3
# 2 4
# 16 32 96

# EXPLANATION
# 2 and 4 divide evenly into 4, 8, 12 and 16.
# 4, 8 and 16 divide evenly into 16, 32, 96.
# 4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.
# PROBLEM DESCRIPTION:
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# n = 5                                     2
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# EXPLANATION: Because the 3rd row is incomplete, we return 2.
# 
# INPUT:                                    OUTPUT:
# n = 8                                     3
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# EXPLANATION: Because the 4th row is incomplete, we return 3.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (left + right) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if curr > n:
                right = k-1
            else:
                left = k+1

        return right
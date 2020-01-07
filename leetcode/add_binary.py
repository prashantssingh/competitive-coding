# PROBLEM DESCRIPTION
# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# EXAMPLE
# INPUT                                             OUTPUT
# a = "11", b = "1"                                 "100"


# Input: 
# Output: "10101"
# INPUT                                             OUTPUT
# a = "1010", b = "1011"                            "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        max_len = max(len(a), len(b))
        a, b = a.zfill(max_len), b.zfill(max_len)
        
        for i in range(max_len-1, -1, -1):
            if a[i] == '1': carry += 1
            if b[i] == '1': carry += 1
            
            carry, remainder = divmod(carry, 2)
            result.append(str(remainder))
            
        if carry == 1: result.append('1')
        
        print("Final:", result)
        return ''.join(result[::-1])
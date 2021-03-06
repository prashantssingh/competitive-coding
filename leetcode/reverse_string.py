# PROBLEM DESCRIPTION
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# ["h","e","l","l","o"]                     ["o","l","l","e","h"]
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# ["H","a","n","n","a","h"]                 ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] =  s[len(s)-i-1], s[i]
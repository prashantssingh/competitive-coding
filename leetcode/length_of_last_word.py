# PROBLEM DESCRIPTION
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length 
# of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# NOTE: A word is defined as a maximal substring consisting of non-space characters only.

# EXAMPLE
# INPUT                                         OUTPUT
# "Hello World"                                 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        
        split_s = s.split()
        if len(split_s) < 1: return 0
        else: return len(split_s[len(split_s)-1])
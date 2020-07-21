#  PROBLEM DESCRIPTION:
# Given two strings s and t , write a function to determine if t is an anagram of s.
# 
# EXAMPLES:
# INPUT                                               OUTPUT:
# s = "anagram", t = "nagaram"                        true
# 
# EXAMPLES:
# INPUT                                               OUTPUT:
# s = "rat", t = "car"                                false
# 
# NOTE:
# You may assume the string contains only lowercase alphabets.
# 
# FOLLOW UP:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        t_dict = dict()
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
            
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
            
        return True
# PROBLEM DESCRIPTION
# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# 
# EXAMPLES:
# INPUT:                                               OUTPUT:
# s = "leetcode"                                       0
# 
# EXAMPLES:
# INPUT:                                               OUTPUT:
# s = "loveleetcode"                                   2
#  
# Note: You may assume the string contains only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i
            
        return -1
                
                
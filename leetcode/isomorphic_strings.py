# PROBLEM DESCRIPTION
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.
# 
# SAMPLE INPUT                                      SAMPLE OUTPUT
# s = "egg", t = "add"                              true
# 
# SAMPLE INPUT                                      SAMPLE OUTPUT
# s = "foo", t = "bar"                              false
# 
# SAMPLE INPUT                                      SAMPLE OUTPUT
# s = "paper", t = "title"                          true
# 
# NOTE:
# You may assume both s and t have the same length.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s or not t: 
            return True
        
        tracker_s = dict()
        tracker_t = dict()
        for i in range(len(s)):
            if (s[i] in tracker_s and tracker_s[s[i]] != t[i]) or (t[i] in tracker_t and tracker_t[t[i]] != s[i]):
                return False
            else:
                tracker_s[s[i]] = t[i]
                tracker_t[t[i]] = s[i]
            
        return True
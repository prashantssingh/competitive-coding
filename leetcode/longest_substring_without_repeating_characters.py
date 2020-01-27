# PROBLEM DESCRIPTION:
# Given a string, find the length of the longest substring without repeating characters.
#
# EXAMPLE:
# Input:                                                  Output:
# "abcabcbb"                                              3
# EXPLANATION - The answer is "abc", with the length of 3. 
#
# Input:                                                  Output:
# "bbbbb"                                                 1
# EXPLANATION - The answer is "b", with the length of 1.
# 
# 
# Input:                                                  Output:
# "pwwkew"                                                3 
# EXPLANATION - The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = set()
        res = curr_str = ''
        for c in s:
            if c not in seen_set:
                print(c)
                seen_set.add(c)
                curr_str += c
                if len(curr_str) > len(res):
                    res = curr_str
            else:
                print(seen_set)
                seen_set.clear()
                curr_str = c
                seen_set.add(c)
                
        return len(res)
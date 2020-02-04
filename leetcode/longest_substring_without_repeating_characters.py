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
        if not s: return 0
        
        i = j = max_len = 0
        seen_set = set()
        while j < len(s):
            if s[j] not in seen_set:
                seen_set.add(s[j])
                j += 1
                max_len = max(len(seen_set), max_len)
            else:
                seen_set.remove(s[i])
                i += 1
        
        return max_len
        
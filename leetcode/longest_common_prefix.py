# PROBLEM DESCRIPTION:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# EXAMPLE:
# INPUT:                                                 OUTPUT:
# ["flower","flow","flight"]                             "fl"
# 
# INPUT:                                                 OUTPUT   
# ["dog","racecar","car"]                                ""
# EXPLANATION: There is no common prefix among the input strings.

# NOTE:
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_str = strs[0]
        res = ""
        for str in strs[1:]:
            max_len = min(len(str), len(curr_str))
            for i in range(max_len):
                if str[i] == curr_str[i]:
                    res += str[i]
                    i += 1
                else:
                    curr_str = res
                    res = ""
                    break
                
        return curr_str
                
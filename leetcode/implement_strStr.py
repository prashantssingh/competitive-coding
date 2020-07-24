# PROBLEM DESCRIPTION:
# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# EXAMPLE:
# INPUT                                                     OUTPUT:
# haystack = "hello", needle = "ll"                         2
# 
# EXAMPLE:
# INPUT                                                     OUTPUT:
# haystack = "aaaaa", needle = "bba"                        -1
# 
# CLARIFICATIONS:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's 
# strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1
# PROBLEM DESCRIPTION
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
# input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Note that an empty string is also considered valid.


# EXAMPLES:

# INPUT                                               OUTPUT:
# "()"                                                true

# INPUT                                               OUTPUT:
# "()[]{}"                                            true
 
# # INPUT                                             OUTPUT:
# "(]"                                                false
 
# # INPUT                                             OUTPUT:
# "([)]"                                              false

# INPUT                                               OUTPUT:
# "{[]}"                                              true

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        parenDict =  {
            ']': '[',
            '}': '{',
            ')': '('
        }
        
        stack = list()
        for char in s:
            # print(char, stack)
            if char in parenDict.keys():
                if not stack:
                    return False
                elif parenDict[char] is not stack.pop():
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        
        return True
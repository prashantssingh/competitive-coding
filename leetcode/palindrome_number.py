# PROBLEM DESCRIPTION:
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the
# same backward as forward.

# EXAMPLE:
# INPUT                                             OUTPUT
# 121                                               true

# INPUT                                             OUTPUT
# -121                                              false
# EXPLANATION: From left to right, it reads -121. From right to left, it becomes 121-. 
# Therefore it is not a palindrome.

# INPUT                                             OUTPUT
# 10                                                false
# Input: -121
# Output: false
# EXPLANATION: Reads 01 from right to left. Therefore it is not a palindrome.


# FOLLOW UP:
# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i, j = 0, len(x)-1
        while i < j:
            # print(f"i: {i}--{x[i]}  ||||   j: {j}--{x[j]}")
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
            
        return True
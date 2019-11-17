# PROBLEM DESCRIPTION
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# 121                                               true 

# SAMPLE INPUT                                      SAMPLE OUTPUT
# 121                                               false
# EXPLANATION
# From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# SAMPLE INPUT                                      SAMPLE OUTPUT
# 10                                                false
# EXPLANATION
# Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:

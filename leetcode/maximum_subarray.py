# PROBLEM DEFINITION:
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has 
# the largest sum and return its sum.

# EXAMPLE
# INPUT                                               OUTPUT:
# [-2,1,-3,4,-1,2,1,-5,4]                             6

# EXPLANATION
# [4,-1,2,1] has the largest sum = 6.

# FOLLOW UP:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer 
# approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp_sum = [0]*len(nums)
        dp_sum[0] = nums[0]
        for i in range(1, len(nums)):
            dp_sum[i] = max(nums[i], nums[i]+dp_sum[i-1])
            
        return max(dp_sum)
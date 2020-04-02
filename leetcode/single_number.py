# PROBLEM DESCRIPTION:
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# 
# NOTE:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# [2,2,1]                                   1
# 
# INPUT:                                    OUTPUT:
# [4,1,2,1,2]                               4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i<len(nums):
            if (i+1 == len(nums)) or (nums[i] != nums[i+1]):
                return nums[i]
            else:
                i += 2
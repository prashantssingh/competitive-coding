# PROBLEM DESCRIPTION
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# EXAMPLE:
# INPUT
# Nums: [2, 7, 11, 15], target: 9,
# 
# EXPLANATION:
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        register = dict()
        for index, elem in enumerate(nums):
            if target-elem in register:
                return [register[target-elem], index]
            else: 
                register[elem] = index
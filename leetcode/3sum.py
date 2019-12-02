# OROBLEM STATEMENT
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# NOTE
# The solution set must not contain duplicate triplets.

# Example:


# EXAMPLES:
# Given array nums = ,
# INPUT                                               OUTPUT:
# [-1, 0, 1, 2, -1, -4]                               [ [-1, 0, 1], [-1, -1, 2] ]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solnSet = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j] + nums[k] == target: solnSet.add(tuple([nums[i], nums[j], nums[k]])); j+=1; k-=1
                elif nums[j] + nums[k] < target: j+=1
                else: k-=1              
                    
        return solnSet
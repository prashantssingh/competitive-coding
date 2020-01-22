# PROBLEM DESCRIPTION:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# LINK: https://leetcode.com/problems/trapping-rain-water/
# ELEVALTION: [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# EXAMPLE:

# INPUT:                                                   OUTPUT:
# [0,1,0,2,1,0,1,3,2,1,2,1]                                6

class Solution:
    def trap(self, height: List[int]) -> int:
        waterTrapped = 0
        if not height:
            return waterTrapped
        
        leftWallMax, rightWallMax =  height[0], height[-1]
        leftWallArray = [0]*len(height)
        rightWallArray = [0]*len(height)
        
        for i in range(1, len(height)):
            if height[i] > leftWallMax: 
                leftWallArray[i] = height[i]
                leftWallMax = height[i]
            else: 
                leftWallArray[i] = leftWallMax
                    
        for i in range(len(height)-1, -1, -1):
            if height[i] > rightWallMax: 
                rightWallArray[i] = height[i]
                rightWallMax = height[i]
            else: 
                rightWallArray[i] = rightWallMax
                    
        # print("LeftWalls:", leftWallArray, ", RightWalls:", rightWallArray)
        
        for i in range(1, len(height)-1):
            minWall = min(leftWallArray[i], rightWallArray[i])
            waterTrapped += minWall - height[i]
            
        return waterTrapped
        
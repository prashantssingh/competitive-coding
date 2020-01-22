# PROBLEM DESCRIPTION
# REFER THIS LINK: https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2963/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height)-1
        while i < j:
            contHeight, contWidth = min(height[i], height[j]), j-i
            area = max(area, contHeight*contWidth)
            if height[i]<height[j]: i+=1
            else: j-=1
            
        return area
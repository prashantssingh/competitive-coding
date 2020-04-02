# PROBLEM DESCRIPTION:
# Given a non-empty array of integers, return the k most frequent elements.
# 
# EXAMPLE:
# INPUT:                                    OUTPUT:
# nums = [1,1,1,2,2,3], k = 2               [1,2]
# 
# INPUT:                                    OUTPUT:
# nums = [1], k = 1                         [1]
# 
# NOTE:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         if not nums: return []
#        
#         freq_dict = dict()
#         for num in nums:
#             freq_dict[num] = freq_dict.get(num, 0) + 1
#        
#         num_freq_list = list()
#         for key in freq_dict:
#             num_freq_list.append((key, freq_dict[key]))
#            
#         num_freq_list = sorted(num_freq_list, key = lambda x: x[1], reverse=True)
#        
#         return [num_freq_list[i][0] for i in range(len(num_freq_list[:k]))]

import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] = freq_dict[num] + 1 
            
        if len(freq_dict) <= k:
            return freq_dict.keys()
        
        heap = []
        for key in freq_dict:
            heapq.heappush(heap, (freq_dict[key], key))
            
            if len(heap) > k:
                heapq.heappop(heap)
           
        res = list()
        while heap:
            res.append(heapq.heappop(heap)[1])
            
        return res[::-1]

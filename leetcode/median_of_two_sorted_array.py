# PROBLEM DESCRIPTION:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).
# 
# EXAMPLES:
# INPUT:                                                 OUTPUT:
# nums1 = [1,3], nums2 = [2]                             2.00000
# EXPLANATION: merged array = [1,2,3] and median is 2.
# 
# INPUT:                                                 OUTPUT:
# nums1 = [1,2], nums2 = [3,4]                           2.50000
#EXPLANATION: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# INPUT:                                                 OUTPUT:
# nums1 = [0,0], nums2 = [0,0]                           0.00000
#  
# INPUT:                                                 OUTPUT:
# nums1 = [], nums2 = [1]                                1.00000
#  
# INPUT:                                                 OUTPUT:
# nums1 = [2], nums2 = []                                2.00000
 

# CONSTRAINTS:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

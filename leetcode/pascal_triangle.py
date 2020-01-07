# PROBLEM DESCRIPTION
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#                     1
#                   1   1
#                 1   2   1
#               1   3   3   1
#             1   4   6   4   1

# EXAMPLE
# INPUT                                         OUTPUT
# 5                                             [
#                                                     [1],
#                                                    [1,1],
#                                                   [1,2,1],
#                                                  [1,3,3,1],
#                                                 [1,4,6,4,1]
#                                                ]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1,1]]
        
        result = [[1], [1,1]]
        for i in range (2, numRows):
            curr = [0]*(i+1)
            curr[0] = curr[i] = 1
            j, k = 1, i-1
            while j <= k:
                curr[j] = curr[k] = result[i-1][j-1] + result[i-1][j]
                j += 1
                k -= 1
            result.append(curr)
            
        return result
        
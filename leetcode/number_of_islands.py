# PROBLEM DESCRIPTION
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is 
# surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You 
# may assume all four edges of the grid are all surrounded by water.

# EXAMPLE 1:
# INPUT                                               OUTPUT:
# 1  1  1  1  0                                       1
# 1  1  0  1  0
# 1  1  0  0  0
# 0  0  0  0  0


# EXAMPLE 2:
# INPUT                                               OUTPUT:
# 1  1  0  0  0                                       3
# 1  1  0  0  0
# 0  0  1  0  0
# 0  0  0  1  1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandMarker = -1
        visitedGrid = grid
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[rowIndex])):
                if rowIndex == 0 and colIndex == 0 and grid[rowIndex][colIndex] == 1:
                    visitedGrid[rowIndex][colIndex] = islandMarker
                    islandMarker += 1
                elif rowIndex > 0 and grid[rowIndex-1][colIndex]<0:
                    visitedGrid[rowIndex][colIndex] = visitedGrid[rowIndex-1][colIndex]
                elif colIndex > 0 and grid[rowIndex][colIndex-1]<0:
                    visitedGrid[rowIndex][colIndex] = visitedGrid[rowIndex][colIndex-1]
                else:
                    visitedGrid[rowIndex][colIndex] = islandMarker
                    islandMarker += 1
                    
        return abs(islandMarker+1)
     
# Above code is failing for below input:
# 1  1  1
# 0  1  0
# 1  1  1

# Optimisation: use recursive method to explore (up, right, bottom, right)
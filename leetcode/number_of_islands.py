# PROBLEM DESCRIPTION
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is 
# surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You 
# may assume all four edges of the grid are all surrounded by water.

# EXAMPLE 1:
# INPUT                                      OUTPUT:
# 11110                                      1
# 11010
# 11000
# 00000


# EXAMPLE 2:
# INPUT                                      OUTPUT:
# 11000                                       3
# 11000
# 00100
# 00011

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
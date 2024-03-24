'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
# Time complexity - O(m * n)
# Space complexity - O(m * n)
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        area = 0
        self.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    area = max(area, self.dfs(grid, i, j))
        
        return area
    
    def dfs(self, grid, i, j):
            if (i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == 0):
                return 0
            
            grid[i][j] = 0
            sum = 1
            for dir in self.directions:
                x = i + dir[0]
                y = j + dir[1]
                sum += self.dfs(grid, x, y)

            # after that we have to add 1 for the current cell to the sum
            return sum

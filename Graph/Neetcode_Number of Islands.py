'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
# Time complexity - O(m*n)
# Space complexity - O(m*n) if all are 1's
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        self.r = len(grid)
        self.c = len(grid[0])
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
            if (i < 0 or j < 0 or i >= self.r or j >= self.c or grid[i][j] == '0'):
                return
            grid[i][j] = '0'
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j-1)   

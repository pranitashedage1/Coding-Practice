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
# Space complexity - O(m*n)
import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        # Initialize the count of islands = 0
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                # for [0, 0 ]- 4 directions
                # [-1, 0], [0, -1], [0, 1], [1, 0]
                # From these only valid directions we will choose which are in the grid
                dicrection = [[-1, 0], [0, -1], [0, 1], [1, 0]]
                for dr, dc in dicrection:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                       grid[r][c] == "1" and 
                       (r, c) not in visited):
                        q.append((r,c))
                        visited.add((r, c))    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands

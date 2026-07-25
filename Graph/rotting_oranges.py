'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #BFS
        queue = deque()
        minutes = 0
        visited = set()
        freshCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                if grid[r][c] == 1:
                    freshCount += 1

        if freshCount == 0:
            return 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def isValid(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x, y) in visited:
                return False
            return True
        
        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for direction in directions:
                    x = r + direction[0]
                    y = c + direction[1]
                    if isValid(x, y):
                        if (x,y) not in visited and grid[x][y] == 1:
                            grid[x][y] = 2
                            queue.append((x,y))
                            visited.add((x,y))
                            freshCount -= 1
            if queue:
                minutes += 1 
                            
        return minutes if freshCount == 0 else -1

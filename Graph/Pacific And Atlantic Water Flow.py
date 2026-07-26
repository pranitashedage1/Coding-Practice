'''
There is an m x n rectangular island that borders both the Pacific 
Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents 
the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells 
directly north, south, east, and west if the neighboring cell's height is less than or 
equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacqueue = deque()
        atlqueue = deque()

        # put left and right column
        for r in range(rows):
            pacqueue.append((r, 0))
            atlqueue.append((r, cols-1))

        for c in range(cols):
            pacqueue.append((0, c))
            atlqueue.append((rows-1, c))

        vP = self.bfs(heights, pacqueue)
        vA = self.bfs(heights, atlqueue)

        res = list()

        for i in range(rows):
            for j in range(cols):
                if vP[i][j] and vA[i][j]:
                    res.append((i, j))

        return res

    
    def bfs(self, heights, queue):
        rows = len(heights)
        cols = len(heights[0])
        visited = [[False]*cols for _ in range(rows)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            r, c = queue.popleft()
            visited[r][c] = True
            for direction in directions:
                x = r + direction[0]
                y = c + direction[1]
                
                if (self.isValid(heights, x, y) and not visited[x][y] and heights[x][y] >= heights[r][c]):
                    queue.append((x, y))
                    visited[x][y] == True

        return visited

    def isValid(self, heights, r, c):
        if r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
            return False
        return True



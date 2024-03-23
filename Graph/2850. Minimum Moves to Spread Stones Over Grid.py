from typing import List
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # Base Case
        t = sum(1 for i in range(3) for j in range(3) if grid[i][j] == 0)
        if t == 0:
            return 0
        
        ans = float('inf')
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    for ni in range(3):
                        for nj in range(3):
                            d = abs(ni - i) + abs(nj - j)
                            if grid[ni][nj] > 1:
                                grid[ni][nj] -= 1
                                grid[i][j] += 1
                                ans = min(ans, d + self.minimumMoves(grid))
                                grid[ni][nj] += 1
                                grid[i][j] -= 1
        return ans

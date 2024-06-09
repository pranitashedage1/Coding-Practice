'''
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
# space complexity - O(1)
# time complexity - O(m*n)
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        while top < bottom and left < right:

            # top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # right col
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (top < bottom and left < right):
                break
            
            # bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # left col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

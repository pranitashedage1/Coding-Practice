'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
'''
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(i, j, board, word, 0):
                    return True
        return False
    
    def search(self, i: int, j: int, board: List[List[str]], word: str, index: int) -> bool:
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        
        temp = board[i][j]
        board[i][j] = '*'
        result = (self.search(i + 1, j, board, word, index + 1) or
                  self.search(i, j + 1, board, word, index + 1) or
                  self.search(i - 1, j, board, word, index + 1) or
                  self.search(i, j - 1, board, word, index + 1))
        
        # Restore the original character since this cell can be visited again
        board[i][j] = temp
        
        return result

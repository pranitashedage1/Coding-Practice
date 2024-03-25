'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''
from typing import List
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Trie()
        self.res = []
        self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, self.root)
        return self.res

    def dfs(self, board: List[List[str]], x: int, y: int, crawl: Trie):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == '*':
            return

        nextC = board[x][y]

        if not crawl or not crawl.children[ord(nextC) - ord('a')]:
            return

        node = crawl.children[ord(nextC) - ord('a')]

        if node.word:
            self.res.append(node.word)
            node.word = None

        board[x][y] = '*'

        self.dfs(board, x + 1, y, node)
        self.dfs(board, x, y + 1, node)
        self.dfs(board, x - 1, y, node)
        self.dfs(board, x, y - 1, node)

        board[x][y] = nextC

    def buildTrie(self, words: List[str]):
        self.root = Trie()
        for word in words:
            crawl = self.root
            for c in word:
                if not crawl.children[ord(c) - ord('a')]:
                    crawl.children[ord(c) - ord('a')] = Trie()
                crawl = crawl.children[ord(c) - ord('a')]
            crawl.word = word

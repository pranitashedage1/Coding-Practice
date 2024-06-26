'''
A transformation sequence from word beginWord to word endWord using a dictionary 
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in 
the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", 
which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''
from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        visited = set()

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue.append(beginWord)
        k = 0

        while queue:
            k += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return k
                self.getNeighs(node, wordSet, queue, visited)
        return 0

    def getNeighs(self, word: str, wordSet: set, queue: deque, visited: set):
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue

                new_word = word[:i] + c + word[i+1:]

                if new_word in wordSet and new_word not in visited:
                    queue.append(new_word)
                    visited.add(new_word)

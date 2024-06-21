'''
Given an array of strings words (without duplicates), return all the concatenated words in the given 
list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words 
(not necessarily distinct) in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:
Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
'''
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        
        # Build Trie for all words
        for word in words:
            if word:
                self.buildTrie(word)
        
        # Find concatenated words
        for word in words:
            if word and self.isConcatenatedWord(word, 0, 0):
                result.append(word)
        
        return result
    
    def isConcatenatedWord(self, word, count, index):
        """
        :type word: str
        :type count: int
        :type index: int
        :rtype: bool
        """
        curr = self.root
        n = len(word)
        
        for i in range(index, n):
            char = word[i]
            if char not in curr.children:
                return False
            curr = curr.children[char]
            if curr.isEnd:
                if i == n - 1:
                    return count >= 1
                if self.isConcatenatedWord(word, count + 1, i + 1):
                    return True
        
        return False
    
    def buildTrie(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True


# Example usage:
# sol = Solution()
# words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# print(sol.findAllConcatenatedWordsInADict(words))


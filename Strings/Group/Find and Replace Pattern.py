'''
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. 
You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every
 letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to 
another letter, and no two letters map to the same letter.

Example 1:
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
 since a and b map to the same letter.

Example 2:
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
'''
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pattern = self.findPattern(pattern)
        result = []
        
        for word in words:
            if pattern == self.findPattern(word):
                result.append(word)
        return result

    def findPattern(self, pattern):
        p = [0] * len(pattern)
        j = 0
        char_map = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in char_map:
                char_map[pattern[i]] = j
                j += 1
            p[i] = char_map[pattern[i]]
        return p

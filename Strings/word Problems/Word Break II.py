'''
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
'''
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.map = {}
        return self.word_Break(s, wordDict, 0)

    def word_Break(self, s: str, wordDict: List[str], start: int) -> List[str]:
        if start in self.map:
            return self.map[start]
        res = []
        if start == len(s):
            res.append("")
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict:
                sublist = self.word_Break(s, wordDict, end)
                for sub in sublist:
                    res.append(s[start:end] + (" " + sub if sub else ""))
        self.map[start] = res
        return res

print(Solution().wordBreak(s="catsanddog", wordDict=["cat","cats","and","sand","dog"]))
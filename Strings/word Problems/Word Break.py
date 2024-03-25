'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = [-1] * len(s)
        self.dict = set(wordDict)
        return self.dfs(s, 0)

    def dfs(self, s: str, start: int) -> bool:
        if start == len(s):
            return True

        if self.memo[start] != -1:
            return self.memo[start] == 1

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in self.dict:
                if self.dfs(s, end):
                    self.memo[start] = 1
                    return True

        self.memo[start] = 0
        return False
    
print(Solution().wordBreak('catsandog', ["cats","dog","sand","and","cat"]))

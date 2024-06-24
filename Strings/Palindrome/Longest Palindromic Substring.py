'''
Given a string s, return the longest 
palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''
class Solution:
    def __init__(self):
        self.max = 0
        self.head = 0

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        for i in range(len(s)):
            self.expandPalindrome(s, i, i + 1)
            self.expandPalindrome(s, i, i)
        return s[self.head:self.head + self.max + 1]
    def expandPalindrome(self, s: str, l: int, r: int):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        # Restore both pointers because they are incremented and decremented 1 extra before breaking the loop
        l += 1
        r -= 1
        if r - l > self.max:
            self.max = r - l
            self.head = l

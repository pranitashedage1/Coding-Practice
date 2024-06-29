'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        if not str:
            return ""

        res = []
        diff = ord('a') - ord('A')
        s1 = list(s)
        for i in range(len(s1)):
            if 'A' <= s[i] <= 'Z':
                s1[i] = chr(ord(s[i]) + diff)

        return ''.join(s1)

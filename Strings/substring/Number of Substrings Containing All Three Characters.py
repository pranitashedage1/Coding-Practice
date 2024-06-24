'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all 
these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b 
and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c 
are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
'''
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = [0, 0, 0]
        l = 0
        r = 0
        res = 0
        extendedPtr = len(s) - 1
        
        while r < len(s):
            count[ord(s[r]) - ord('a')] += 1
            
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                count[ord(s[l]) - ord('a')] -= 1
                res += extendedPtr - r + 1
                l += 1
            
            r += 1
        return res


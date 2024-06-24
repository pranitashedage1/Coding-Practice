'''
Given a string s, return true if a permutation of the string could form a 
palindrome and false otherwise.

Example 1:
Input: s = "code"
Output: false

Example 2:
Input: s = "aab"
Output: true

Example 3:
Input: s = "carerac"
Output: true
'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        count_odd = 0
        for i in range(len(count)):
            if count[i] % 2 != 0:
                count_odd += 1

        return count_odd <= 1

'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_length = 0
        max_length = 0
        set1 = set()
        for right in range(len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
            set1.add(s[right])
            max_length = max(max_length, right-left+1)
            right += 1
        return max_length

print(Solution().lengthOfLongestSubstring('abcabcbb'))

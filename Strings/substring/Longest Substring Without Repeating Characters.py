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
# Time complexity - O(n)
# Space Complexity - O(1) where k is the size of set
class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        freq_count = {}
        count = 0
        maxLength = 0
        while end < len(s):
            char = s[end]
            freq_count[char] = freq_count.get(char, 0) + 1
            if freq_count[char] > 1:
                count += 1
            end += 1
            while count > 0:
                temp = s[start]
                start += 1
                if freq_count[temp] > 1:
                    count -= 1
                freq_count[temp] -= 1
            maxLength = max(maxLength, end - start)
        return maxLength

print(Solution().lengthOfLongestSubstring('abcabcbb'))

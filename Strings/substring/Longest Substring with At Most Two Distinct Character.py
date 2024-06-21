'''
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
'''
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        start, end, count, maxLength = 0, 0, 0, 0
        char_dict = {}
        while end < len(s):
            char = s[end]
            char_dict[char] = char_dict.get(char, 0) + 1
            if  char_dict[char] == 1:
                count += 1
            end += 1
            while count > 2:
                temp_char = s[start]
                char_dict[temp_char] = char_dict.get(temp_char) - 1 
                if char_dict[temp_char] == 0:
                    count -= 1
                start += 1      
            maxLength = max(maxLength, end-start)
        return maxLength

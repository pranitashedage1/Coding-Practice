'''
Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Initialize variables
        map = defaultdict(int)
        start = end = maxLen = count = 0

        # Sliding window approach
        while end < len(s):
            temp = s[end]
            map[temp] += 1
            if map[temp] == 1:
                count += 1
            end += 1
            # If number of distinct characters exceeds k, move start pointer
            while count > k:
                c = s[start]
                map[c] -= 1
                if map[c] == 0:
                    count -= 1
                start += 1
            # Update max length
            maxLen = max(maxLen, end - start)
        return maxLen
